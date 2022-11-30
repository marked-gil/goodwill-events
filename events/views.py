from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView, View
from datetime import datetime, date, time
from .models import Event, Comment
from seating.models import EventSeating
from .forms import CommentForm


class FeaturedView(TemplateView):
    """
    Renders the featured events in the Home page, and recycles expired events
    and deletes their booked seats.
    """
    template_name = 'index.html'

    @staticmethod
    def _recycle_expired_event(event, date_of_event):
        """
        Modifies event's date to next year of same month and day
        and updates the database
        """
        event.event_date = date_of_event.replace(
            date_of_event.year + 1)
        event.save()

    @staticmethod
    def _delete_booked_seats(event):
        """
        Deletes all seats reserved for the event from
        the database
        """
        event_seats_queryset = EventSeating.objects.filter(event=event)
        for qset in event_seats_queryset:
            qset.delete()

    def get_context_data(self, **kwargs):
        """
        Adds the featured events into the context dict, and automatically
        recycles expired events by changing their date to the following year
        """

        # Automatcally recycles the expired event to next year
        all_events = Event.objects.all()

        for event in all_events:
            date_of_event = event.event_date
            event_expiration_time = event.event_time

            if date_of_event < date.today():
                self._recycle_expired_event(event, date_of_event)
                self._delete_booked_seats(event)
            elif date_of_event == date.today():
                if datetime.now().time() >= event_expiration_time:
                    self._recycle_expired_event(event, date_of_event)
                    self._delete_booked_seats(event)

        # Inserts the featured events into the context dictionary
        context = super().get_context_data(**kwargs)
        context['featured_events'] = Event.objects.filter(
            status=1).reverse()[:3]

        return context


class EventsList(ListView):
    """
    Renders a list of all event objects in the Events page template
    """
    model = Event
    context_object_name = 'events_list'
    queryset = Event.objects.filter(status=1).order_by('event_date')
    template_name = 'events/events.html'
    paginate_by = 5


class EventDetails(DetailView):
    """
    Displays the details of the specified Event
    """
    model = Event
    context_object_name = 'event'
    template_name = 'events/event_details.html'

    def get_context_data(self, **kwargs):
        """
        Retrieves and adds the following objects into the context dict so it
        can be used in the template: liked, comments, and number of seats
        available.
        """
        context = super().get_context_data(**kwargs)
        event_post = Event.objects.filter(status=1).get(
            slug=self.kwargs.get('slug'))
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
    """
    Likes or unlikes an event post.
    """
    def post(self, request, slug):
        """
        Accepts POST method to 'Like' or 'Unlike' an event post.
        """
        event = get_object_or_404(Event, slug=slug)

        if event.likes.filter(id=request.user.id).exists():
            event.likes.remove(request.user)
        else:
            event.likes.add(request.user)

        return redirect(reverse('event_details', args=[slug]))


class CommentView(LoginRequiredMixin, View):
    """
    Adds user's comment to an event post.
    """
    def post(self, request, slug):
        """
        Accepts POST method to add user's comment to an event post.
        """
        event = get_object_or_404(Event, slug=slug)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment_form.instance.event = event
            comment_form.save()
        return redirect(reverse('event_details', args=[slug]))


class DeleteComment(LoginRequiredMixin, View):
    """
    Deletes a user's comment to an event post.
    """
    def post(self, request, pk):
        """
        Accepts POST method to delete a user's comment to an event post.
        """
        user_comment = get_object_or_404(Comment, id=pk)

        if user_comment.author == request.user:
            user_comment.delete()

        return redirect(self.request.META.get('HTTP_REFERER'))
