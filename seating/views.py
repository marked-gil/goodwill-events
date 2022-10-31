from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from events.models import Event
from .models import EventSeating
from .forms import SeatReserveForm


class EventSeatsView(View):

    def get(self, request, slug, *args, **kwargs):
        reservation_form = SeatReserveForm()
        try:
            event = Event.objects.filter(slug=slug).first()
            event_seats_obj = EventSeating.objects.filter(event__slug=slug)
            if not event_seats_obj.exists():
                raise Exception("Start making seat reservations for this event.")
        except Exception as info:
            messages.info(request, info)
            return render(request, './seating/reserve-seats.html', {
                'event': event, 'form': reservation_form
                })
        else:
            list_seats = []
            for item in event_seats_obj:
                list_seats.append(str(item.seat_location_1))
                if item.seat_location_2:
                    list_seats.append(str(item.seat_location_2))
            return render(request, './seating/reserve-seats.html', {
                'data': list_seats,
                'event': event, 'form': reservation_form
                })

    def post(self, request, slug, *args, **kwargs):
        event = Event.objects.filter(slug=slug).first()
        user = request.user
        reservation_form = SeatReserveForm(data=request.POST)
        if reservation_form.is_valid():
            filled_form = reservation_form.save(commit=False)
            filled_form.event = event
            filled_form.reserved_by = user
            try:
                filled_form.save()
                messages.success(
                    request, f"New seats are reserved for {event}.")
            except Exception:
                messages.error(
                    request, "You already booked 2 seats for this event.")
                return redirect(request.path_info)
            else:
                return redirect('/')
        return redirect(request.path_info)
