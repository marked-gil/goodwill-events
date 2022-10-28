from django.shortcuts import render
from django.contrib import messages
from django.views import View
from events.models import Event
from .models import EventSeating


class EventSeatsView(View):
    def get(self, request, slug, *args, **kwargs):
        try:
            event = Event.objects.filter(slug=slug).first()
            event_seats_obj = EventSeating.objects.filter(event__slug=slug)
            if not event_seats_obj.exists():
                raise Exception("Start making seat reservations for this event.")
        except Exception as info:
            return render(request, './seating/reserve-seats.html', {
                'event': event
                })
        else:
            list_seats = []
            for item in event_seats_obj:
                list_seats.append(str(item.seat_location))
            return render(request, './seating/reserve-seats.html', {
                'data': list_seats,
                'event': event,
                })
