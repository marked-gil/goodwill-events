from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Event


class FeaturedView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_events'] = Event.objects.all()[:3]
        return context
