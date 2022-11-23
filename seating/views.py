from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.views import View
from events.models import Event
from .models import EventSeating
from .forms import SeatReserveForm
from django.core.mail import send_mail
from django.conf import settings


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
                    "Reservations can be updated.a"
                )

        except Exception as info:
            if user_booked_seats.exists():
                return redirect(
                    f'/{self.kwargs.get("slug")}/update-reservation/'
                    )
            else:
                return render(request, 'reserve-seats.html', {
                    'event': event, 'form': reservation_form})

        else:
            list_seats = []
            for item in event_seats_obj:
                list_seats.append(str(item.seat_location_1))
                if item.seat_location_2:
                    list_seats.append(str(item.seat_location_2))

            return render(request, 'reserve-seats.html', {
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

        return render(request, 'reserve-seats.html', {
            'data': list_seats, 'event': event, 'form': reservation_form,
            'user_booked_seats': user_booked_seats})

    def post(self, request, slug, *args, **kwargs):
        user = request.user
        event_seats_obj = EventSeating.objects.filter(
            event__slug=slug)
        user_reservation = event_seats_obj.filter(
            reserved_by=user).first()

        reservation_form = SeatReserveForm(
            request.POST, instance=user_reservation)

        try:
            if reservation_form.is_valid():
                updated_form = reservation_form.save(commit=False)
                updated_form.save()
            else:
                raise Exception
        except Exception:
            formdata_dict = dict(request.POST)
            empty_seat_1 = formdata_dict['seat_location_1'] == ['']
            empty_seat_2 = formdata_dict['seat_location_2'] == ['']
            if (empty_seat_1 and empty_seat_2):
                return redirect(f'/{self.kwargs.get("slug")}/delete-reservation/')
        else:
            return redirect(request.path_info)


class DeleteSeatsReservation(LoginRequiredMixin, DeleteView):
    model = EventSeating

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        event_seats_obj = EventSeating.objects.filter(
            event__slug=slug)
        return event_seats_obj

    def delete(self, request, slug, *args, **kwargs):
        event_seats_obj = EventSeating.objects.filter(
            event__slug=slug)
        self.object = event_seats_obj.filter(
            reserved_by=request.user).first()
        self.object.delete()
        messages.success(request,
                         'Your reservation for this event is deleted successfully.'
                         )
        return redirect(f'/{self.kwargs.get("slug")}/reserve-seat/')
