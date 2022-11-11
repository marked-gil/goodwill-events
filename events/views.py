from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView, View
from .models import Event, Comment
from .forms import CommentForm


class FeaturedView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_events'] = Event.objects.all().reverse()[:3]
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
        event_post = Event.objects.get(slug=self.kwargs.get('slug'))
        likers = event_post.likes.all()

        if self.request.user in likers:
            context['liked'] = True
        else:
            context['liked'] = False

        context['comments'] = Comment.objects.filter(
            event__slug=self.kwargs.get('slug'))

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
