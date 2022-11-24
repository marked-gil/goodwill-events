from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView, View
from datetime import datetime, date, time
from .models import Event, Comment
from seating.models import EventSeating
from .forms import CommentForm


class FeaturedView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):

        # Automatcally recycles the expired event to next year
        all_events = Event.objects.all()
        for event in all_events:
            date_of_event = event.event_date
            event_expiration = time(hour=22, minute=0)

            if date_of_event < date.today():
                event.event_date = date_of_event.replace(
                    date_of_event.year + 1)
                event.save()
            elif date_of_event == date.today():
                if datetime.now().time() >= event_expiration:
                    event.event_date = date_of_event.replace(
                        date_of_event.year + 1)
                    event.save()

        # Retrieves the featured events
        context = super().get_context_data(**kwargs)
        context['featured_events'] = Event.objects.filter(status=1).reverse()[:3]

        return context


class EventsList(ListView):
    model = Event
    context_object_name = 'events_list'
    queryset = Event.objects.filter(status=1).order_by('event_date')
    template_name = 'events.html'
    paginate_by = 2


class EventDetails(DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'event_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event_post = Event.objects.filter(status=1).get(slug=self.kwargs.get('slug'))
        likers = event_post.likes.all()

        # checks if the user has already liked a post
        if self.request.user in likers:
            context['liked'] = True
        else:
            context['liked'] = False

        # retrieves the comments for the event post
        context['comments'] = Comment.objects.filter(
            event__slug=self.kwargs.get('slug'))

        # retrieves the number of seats still available
        self.TOTAL_SEATS_AVAILABLE = 142
        seat_reservations = EventSeating.objects.filter(
            event__slug=self.kwargs.get('slug'))

        for reserv in seat_reservations:
            if reserv.seat_location_1 is not None:
                self.TOTAL_SEATS_AVAILABLE -= 1
            if reserv.seat_location_2 is not None:
                self.TOTAL_SEATS_AVAILABLE -= 1

        context['seats_available'] = self.TOTAL_SEATS_AVAILABLE

        return context


class EventLike(LoginRequiredMixin, View):

    def post(self, request, slug):
        event = get_object_or_404(Event, slug=slug)

        if event.likes.filter(id=request.user.id).exists():
            event.likes.remove(request.user)
        else:
            event.likes.add(request.user)

        return redirect(reverse('event_details', args=[slug]))


class CommentView(LoginRequiredMixin, View):

    def post(self, request, slug):
        event = get_object_or_404(Event, slug=slug)
        comment_form = CommentForm(request.POST)
        print(comment_form)

        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment_form.instance.event = event
            comment_form.save()
        return redirect(reverse('event_details', args=[slug]))


class DeleteComment(LoginRequiredMixin, View):

    def post(self, request, pk):
        user_comment = get_object_or_404(Comment, id=pk)

        if user_comment.author == request.user:
            user_comment.delete()

        return redirect(self.request.META.get('HTTP_REFERER'))
