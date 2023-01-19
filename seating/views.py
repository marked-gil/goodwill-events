from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, View, DeleteView
from django.contrib import messages
from events.models import Event
from .models import EventSeating
from .forms import SeatReserveForm


class EventSeatsView(LoginRequiredMixin, TemplateView):
    """
    Displays the specific event's Seat Map page (Seat Reservation page)
    and its reserved seats.
    """

    template_name = 'seating/reserve-seats.html'
    permission_denied_message = 'SIGN IN to make seat reservations.'

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
        Retrieves the contents for the event's Seat Map page
        (Seat Reservation page) and pass them to the 'context' object for use
        in the displayed template
        """
        context = self.get_context_data(**kwargs)

        context['form'] = SeatReserveForm()

        event = Event.objects.filter(slug=slug).first()
        context['event'] = event
        event_seats_obj = EventSeating.objects.filter(event__slug=slug)
        context['user_booked_seats'] = event_seats_obj.filter(
            reserved_by=request.user)

        event_booked_seats = []
        for item in event_seats_obj:
            event_booked_seats.append(str(item.seat_location_1))
            if item.seat_location_2:
                event_booked_seats.append(str(item.seat_location_2))
        context['data'] = event_booked_seats

        return self.render_to_response(context)


class ReserveSeats(LoginRequiredMixin, View):
    """
    Processes and saves new reservation made by a user for an event
    """

    def post(self, request, slug, *args, **kwargs):
        """
        Saves to database the seat/s booked by the user in response to a POST
        request method.
        """
        success_url = f'/{self.kwargs.get("slug")}/seat-reservation/'

        event = Event.objects.filter(slug=slug).first()
        user = request.user
        reservation_form = SeatReserveForm(data=request.POST)
        if reservation_form.is_valid():
            filled_form = reservation_form.save(commit=False)
            filled_form.event = event
            filled_form.reserved_by = user
            filled_form.save()
            messages.success(
                request, f"Reservation is made for {event}."
                )
        return redirect(success_url)


class UpdateSeatsReservation(LoginRequiredMixin, View):
    """
    Updates the database when the user makes changes to their seat reservation
    """

    def post(self, request, slug, *args, **kwargs):
        """
        Updates the user's seat reservation/s on the database in response to
        POST request.
        """
        seat_reservation_URL = f'/{self.kwargs.get("slug")}/seat-reservation/'

        user = request.user
        event_seats_obj = EventSeating.objects.filter(
            event__slug=slug)
        user_reservation = event_seats_obj.filter(
            reserved_by=user).first()

        reservation_form = SeatReserveForm(
            request.POST, instance=user_reservation)

        if reservation_form.is_valid():
            updated_form = reservation_form.save(commit=False)
            updated_form.save()

            msg = 'Your reservation for this event is successfully UPDATED.'
            messages.success(request, msg)

        else:
            msg = 'Your reservation for this event is successfully UPDATED.'
            messages.success(request, msg)

        return redirect(seat_reservation_URL)


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
        success_URL = f'/{self.kwargs.get("slug")}/seat-reservation/'

        try:
            self.object.delete()
        except Exception:
            error_msg = "Seat cancellation is NOT successful. Try again."
            messages.error(request, error_msg)
        else:
            succcess_msg = "You have successfully CANCELLED your reservation."
            messages.success(request, succcess_msg)

        return redirect(success_URL)
