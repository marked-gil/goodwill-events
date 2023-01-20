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

    def test_home_page(self):
        """
        Tests the correct rendering of the Home page
        """
        url = reverse('featured_events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/index.html')
        self.assertContains(response, 'Featured Events')

    def test_events_page(self):
        """
        Tests the correct rendering of the Events page
        """
        url = reverse('events_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/events.html')
        self.assertContains(response, 'Upcoming Events')

    def test_view_seatmap(self):
        """
        Tests the correct rendering of the generic Seat Map page
        """
        url = reverse('view_seatmap')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/view_seatmap.html')
        self.assertContains(response, 'Seat Map')
