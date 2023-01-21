from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from events.models import Event
from datetime import date, time, timedelta


class TestSeatReservation(TestCase):
    """
    Tests the Seat Reservation Page
    """
    def setUp(self):
        """
        Provides the necessary variables, creates a new user and event, and
        logs in the user
        """
        self.login_url = '/accounts/login/'
        self.username = 'voltes_v'
        self.email = 'mark@mail.com'
        self.password = 'japanes3_anime145$'

        User.objects.create_user(
            username=self.username, email=self.email, password=self.password
            )

        # User Login
        self.client.post(self.login_url, {
            'login': self.username, 'password': self.password
            })

        # Create an Event
        self.test_event = Event.objects.create(
            title='Test Event',
            slug='test-event',
            blurb='A Big Test Event',
            event_date=date.today() + timedelta(days=365),
            event_time=time(19, 0),
            post_content='Test event details here',
            author='Mark G',
            entered_by=User.objects.filter(username=self.username).first(),
            status=1)

    def test_seat_reservation_page(self):
        """ Test the rendering of the Seat Reservation Page """
        response = self.client.get(
            f'/{self.test_event.slug}/seat-reservation/')
        self.assertTrue(response, 200)
        self.assertTemplateUsed(response, 'seating/reserve-seats.html')
        self.assertContains(response, 'Click the box to select the seat.')
