from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView, View
from datetime import datetime, date, time
from .models import Event, Comment
from seating.models import EventSeating
from .forms import CommentForm


class FeaturedView(TemplateView):
    """
    Renders the featured events in the Home page, and recycles expired events
    and deletes their booked seats.
    """
    template_name = 'events/index.html'

    @staticmethod
    def _add_one_year(event, date_of_event):
        """
        Modifies event's date to next year with same month and day,
        and updates the database
        """
        event.event_date = date_of_event.replace(
            datetime.now().year + 1)
        event.save()

    @staticmethod
    def _delete_booked_seats(event):
        """
        Deletes all seats reserved for the event from
        the database
        """
        event_seats_queryset = EventSeating.objects.filter(event=event)
        for qset in event_seats_queryset:
            qset.delete()

    @staticmethod
    def _delete_event_likes(event):
        """
        Removes all likes for the event from the database
        """
        event_obj = Event.objects.get(id=event.id)
        event_obj.likes.clear()

    @staticmethod
    def _delete_comments(event):
        """
        Deletes all the comments for the event from the database
        """
        comment_queryset = Comment.objects.filter(event=event)
        for qset in comment_queryset:
            qset.delete()

    @staticmethod
    def _recycle_expired_event(obj, show, event_date):
        """
        Recyles the expired event by moving event's date to next year,
        and deleting all its booked seats, likes, and comments
        """
        obj._add_one_year(show, event_date)
        obj._delete_booked_seats(show)
        obj._delete_event_likes(show)
        obj._delete_comments(show)

    def get_context_data(self, **kwargs):
        """
        Adds the featured events into the context dict, and automatically
        recycles expired events
        """
        all_events = Event.objects.all()

        for event in all_events:
            date_of_event = event.event_date
            event_expiration_time = event.event_time

            if date_of_event < date.today():
                self._recycle_expired_event(self, event, date_of_event)
            elif date_of_event == date.today():
                if datetime.now().time() >= event_expiration_time:
                    self._recycle_expired_event(self, event, date_of_event)

        # Inserts the featured events into the context dictionary
        context = super().get_context_data(**kwargs)
        context['featured_events'] = Event.objects.filter(
            status=1).reverse()[:3]

        return context


class EventsList(ListView):
    """
    Renders a list of active (unexpired) events in the Events page,
    and filters them as per user search query
    """
    model = Event
    context_object_name = 'events_list'
    queryset = queryset = Event.objects.filter(status=1).exclude(
        event_date__lte=date.today()).order_by('event_date')
    template_name = 'events/events.html'
    paginate_by = 5


class SearchEvents(ListView):
    """
    Filters the events as per user's search, and renders the template with
    the list of corresponding events
    """
    model = Event
    context_object_name = 'events_list'
    template_name = 'events/events.html'
    paginate_by = 4

    month_dict = {
            'January': 1,
            'February': 2,
            'March': 3,
            'April': 4,
            'May': 5,
            'June': 6,
            'July': 7,
            'August': 8,
            'September': 9,
            'October': 10,
            'November': 11,
            'December': 12
        }

    def get_queryset(self):
        """
        Retrieves the queryset to be rendered on the Events page
        """
        queryset = super().get_queryset()
        search_value = self.request.GET.get('filter_events', '')

        try:
            search_month = self.month_dict[search_value]
        except KeyError:
            if search_value == 'all-events' or search_value == '':
                queryset = Event.objects.filter(status=1).exclude(
                    event_date__lte=date.today()).order_by('event_date')
            else:
                queryset = ''
        else:
            queryset = queryset.filter(event_date__month=search_month).exclude(
                event_date__lte=date.today()).order_by('event_date')

        return queryset

    def get_context_data(self, **kwargs):
        """
        Displays the queried 'month' on the Events page, or a message if query
        is invalid
        """
        context = super().get_context_data(**kwargs)
        search_month = self.request.GET.get('filter_events')

        if search_month in self.month_dict:
            context['search_month'] = search_month
        elif search_month is None:
            context['search_month'] = ''
        elif search_month != 'all-events':
            message = 'Invalid query'
            context['search_month'] = message

        context['filter_events'] = '&filter_events='

        return context


class EventDetails(DetailView):
    """
    Displays the details of the specified Event
    """
    model = Event
    context_object_name = 'event'
    template_name = 'events/event_details.html'

    def get_context_data(self, **kwargs):
        """
        Retrieves and adds the following objects into the context dict so it
        can be used in the template: liked, comments, and number of seats
        available.
        """
        context = super().get_context_data(**kwargs)
        event_post = Event.objects.filter(status=1).get(
            slug=self.kwargs.get('slug'))
        likers = event_post.likes.all()

        # checks if the user has already liked a post
        if self.request.user in likers:
            context['liked'] = True
        else:
            context['liked'] = False

        # retrieves the comments for the event post
        context['comments'] = Comment.objects.filter(
            event__slug=self.kwargs.get('slug'))

        # retrieves the number of seats still available
        self.TOTAL_SEATS_AVAILABLE = 142
        seat_reservations = EventSeating.objects.filter(
            event__slug=self.kwargs.get('slug'))

        for reserv in seat_reservations:
            if reserv.seat_location_1 is not None:
                self.TOTAL_SEATS_AVAILABLE -= 1
            if reserv.seat_location_2 is not None:
                self.TOTAL_SEATS_AVAILABLE -= 1

        context['seats_available'] = self.TOTAL_SEATS_AVAILABLE

        return context


class EventLike(LoginRequiredMixin, View):
    """
    Likes or unlikes an event post.
    """
    def post(self, request, slug):
        """
        Accepts POST method to 'Like' or 'Unlike' an event post.
        """
        event = get_object_or_404(Event, slug=slug)

        if event.likes.filter(id=request.user.id).exists():
            event.likes.remove(request.user)
        else:
            event.likes.add(request.user)

        return redirect(reverse('event_details', args=[slug]))


class CommentView(LoginRequiredMixin, View):
    """
    Adds user's comment to an event's post.
    """
    def post(self, request, slug):
        """
        Accepts POST method to add user's comment to an event post.
        """
        event = get_object_or_404(Event, slug=slug)
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment_form.instance.author = request.user
            comment_form.instance.event = event
            comment_form.save()
            return JsonResponse({'message': 'success'})

        return JsonResponse({'message': 'The submitted form is invalid.'})


class DeleteComment(LoginRequiredMixin, View):
    """
    Deletes a user's comment to an event post.
    """
    def post(self, request, pk):
        """
        Accepts POST method to delete a user's comment to an event post.
        """
        user_comment = get_object_or_404(Comment, id=pk)

        if user_comment.author == request.user:
            user_comment.delete()

        return JsonResponse({'message': 'success'})


class SeatMapView(TemplateView):
    """
    Displays the generic seatmap
    """
    template_name = "events/view_seatmap.html"
