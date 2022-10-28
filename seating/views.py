from django.shortcuts import render
from django.views import View
from .models import EventSeating


class EventSeatsView(View):
    def get(self, request, slug, *args, **kwargs):
        event_seats_obj = EventSeating.objects.filter(event__slug=slug)
        list_seats = []
        for item in event_seats_obj:
            list_seats.append(str(item.seat_location))
            if num_iteration == 1:
                event_name = item.event
        return render(request, './seating/reserve-seats.html', {
            'data': list_seats,
            'event': event_name,
            })
