from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models import Event


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

        return context
