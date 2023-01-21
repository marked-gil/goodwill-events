from django.test import TestCase
from .models import Event
from datetime import datetime, date, time
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client


class TestEventsViews(TestCase):
    """
    Tests Views that belong to 'events' app
    """
    def setUp(self):
        self.home_url = reverse('featured_events')
        self.events_url = reverse('events_list')
        self.generic_seatmap_url = reverse('view_seatmap')
        self.specific_event_url_name = 'event_details'

    def test_home_page(self):
        """
        Tests the correct rendering of the Home page
        """
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/index.html')
        self.assertContains(response, 'Featured Events')

    def test_events_page(self):
        """
        Tests the correct rendering of the Events page
        """
        response = self.client.get(self.events_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/events.html')
        self.assertContains(response, 'Upcoming Events')

    def test_view_seatmap(self):
        """
        Tests the correct rendering of the generic Seat Map page
        """
        response = self.client.get(self.generic_seatmap_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/view_seatmap.html')
        self.assertContains(response, 'Seat Map')

    def test_specific_event_page(self):
        """
        Tests the correct rendering of the Event Details page
        """
        response = self.client.get(reverse(
            self.specific_event_url_name, kwargs={'slug': 'test-event'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('events/event_details.html')
