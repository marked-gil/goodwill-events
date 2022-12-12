from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView
from django.views import View
from django.contrib import messages
from events.models import Event
from .models import EventSeating
from .forms import SeatReserveForm
from django.core.mail import send_mail
from django.conf import settings


class EventSeatsView(LoginRequiredMixin, View):
    """
    Displays the seat map page and all the seats reserved for a particular
    event as requested by a logged-in user.
    Also redirects to the UpdateSeatsReservation view if the logged-in user
    has already booked a seat/s for the event.
    """
    permission_denied_message = 'You need to sign in to make seat reservations.'

    def dispatch(self, request, *args, **kwargs):
        """
        Displays a message to tell user to sign in before making reservation
        """
        if not request.user.is_authenticated:
            messages.error(request, self.permission_denied_message)
            return self.handle_no_permission()
        return super(EventSeatsView, self).dispatch(request, *args, **kwargs)

    def get(self, request, slug, *args, **kwargs):
        """
        Retrieves the requested event and its reserved seats, and returns the
        Seat Reservation template with details of the specific event.
        Redirects to the UpdateReservationView if user has already booked
        seat/s for the event.
        """
        reservation_form = SeatReserveForm()
        try:
            event = Event.objects.filter(slug=slug).first()
            event_seats_obj = EventSeating.objects.filter(event__slug=slug)
            user_booked_seats = event_seats_obj.filter(
                reserved_by=request.user)

            if user_booked_seats.exists():
                raise Exception(
                    "Reservations can be updated."
                )

        except Exception as info:
            return redirect(
                f'/{self.kwargs.get("slug")}/update-reservation/'
                )

        else:
            list_seats = []
            for item in event_seats_obj:
                list_seats.append(str(item.seat_location_1))
                if item.seat_location_2:
                    list_seats.append(str(item.seat_location_2))

            return render(request, 'seating/reserve-seats.html', {
                'data': list_seats, 'event': event, 'form': reservation_form
                })

    def post(self, request, slug, *args, **kwargs):
        """
        Saves to database the seat/s booked by the user in response to a POST
        request method.
        """
        event = Event.objects.filter(slug=slug).first()
        user = request.user
        reservation_form = SeatReserveForm(data=request.POST)
        if reservation_form.is_valid():
            filled_form = reservation_form.save(commit=False)
            filled_form.event = event
            filled_form.reserved_by = user
            filled_form.save()
            messages.success(
                request, f"New seats are reserved for {event}."
                )
        return redirect(request.path_info)


class UpdateSeatsReservation(LoginRequiredMixin, View):
    """
    Displays the seat/s reserved by the logged-in user, and updates the
    database if the user makes changes to their seat reservation.
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Retrieves the requested event and user's booked seats and returns the
        Seat Reservation template for updating the booked seats.
        """
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

        return render(request, 'seating/reserve-seats.html', {
            'data': list_seats, 'event': event, 'form': reservation_form,
            'user_booked_seats': user_booked_seats})

    def post(self, request, slug, *args, **kwargs):
        """
        Updates the user's seat reservation/s for a particular event in the
        database in response to POST request.
        Redirects to DeleteSeatsReservation view if reservation form is
        emptied.
        """
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
                raise Exception(
                    "Reservation form is empty. This may mean you want to delete your reserved seats."
                )
        except Exception:
            formdata_dict = dict(request.POST)
            empty_seat_1 = formdata_dict['seat_location_1'] == ['']
            empty_seat_2 = formdata_dict['seat_location_2'] == ['']
            if (empty_seat_1 and empty_seat_2):
                return redirect(
                    f'/{self.kwargs.get("slug")}/delete-reservation/'
                    )
        else:
            messages.success(request,
                             'Reservation for this event is successfully UPDATED.'
                             )
            return redirect(request.path_info)


class DeleteSeatsReservation(LoginRequiredMixin, DeleteView):
    """
    Deletes the seats reserved by a logged-in user for a particular event
    """

    model = EventSeating

    def get_object(self, queryset=None):
        """
        Retrieves and returns the seats booked for a particular event
        """
        slug = self.kwargs.get('slug')
        event_seats_obj = EventSeating.objects.filter(
            event__slug=slug)

        return event_seats_obj

    def delete(self, request, *args, **kwargs):
        """
        Deletes the seats reserved by the user for an event.
        """
        self.object = self.get_object().filter(
            reserved_by=request.user
            ).first()
        success_url = f'/{self.kwargs.get("slug")}/reserve-seat/'

        try:
            self.object.delete()
        except Exception:
            error_msg = "Something went wrong. Seat cancellation is NOT successful."
            messages.error(request, error_msg)
        else:
            succcess_msg = "You have successfully CANCELLED your reservation."
            messages.success(request, succcess_msg)
        return redirect(success_url)
