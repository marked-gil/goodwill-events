from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from events.models import Event
from .models import EventSeating
from .forms import SeatReserveForm


class EventSeatsView(LoginRequiredMixin, View):
    permission_denied_message = 'You need to sign in to make seat reservations.'

    # Displays a message to tell user to sign in before making reservation
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.permission_denied_message)
            return self.handle_no_permission()
        return super(EventSeatsView, self).dispatch(request, *args, **kwargs)

    def get(self, request, slug, *args, **kwargs):
        reservation_form = SeatReserveForm()
        try:
            event = Event.objects.filter(slug=slug).first()
            event_seats_obj = EventSeating.objects.filter(event__slug=slug)
            user_booked_seats = event_seats_obj.filter(
                reserved_by=request.user)

            if not event_seats_obj.exists():
                raise Exception(
                    "Start making seat reservations for this event."
                )
            elif user_booked_seats.exists():
                raise Exception(
                    "You may update your reserved seats."
                )

        except Exception as info:
            messages.info(request, info)
            if user_booked_seats.exists():
                return redirect(
                    f'/{self.kwargs.get("slug")}/update-reservation/'
                    )
            else:
                return render(request, './seating/reserve-seats.html', {
                    'event': event, 'form': reservation_form})

        else:
            list_seats = []
            for item in event_seats_obj:
                list_seats.append(str(item.seat_location_1))
                if item.seat_location_2:
                    list_seats.append(str(item.seat_location_2))

            return render(request, './seating/reserve-seats.html', {
                'data': list_seats, 'event': event, 'form': reservation_form
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


class UpdateSeatsReservation(LoginRequiredMixin, View):

    def get(self, request, slug, *args, **kwargs):
        reservation_form = SeatReserveForm()

        event = Event.objects.filter(slug=slug).first()
        event_seats_obj = EventSeating.objects.filter(event__slug=slug)
        user_booked_seats = event_seats_obj.filter(
            reserved_by=request.user)

        list_seats = []
        for item in event_seats_obj:
            list_seats.append(str(item.seat_location_1))
            if item.seat_location_2:
                list_seats.append(str(item.seat_location_2))

        return render(request, './seating/reserve-seats.html', {
            'data': list_seats, 'event': event, 'form': reservation_form,
            'user_booked_seats': user_booked_seats})
