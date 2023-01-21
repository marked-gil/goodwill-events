from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from events.models import Event, Comment
from datetime import date, time, timedelta


class TestEventsViews(TestCase):
    """
    Tests Views that belong to 'events' app
    """
    def setUp(self):
        """ Provides the URLs for testing """
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


class TestEventPageFeatures(TestCase):
    """
    Tests the features/functionalities on the specific event page
    """
    def setUp(self):
        """
        Sets up the variables, creates user and logs in, and creates an event
        """
        # URLs
        self.login_url = '/accounts/login/'
        self.specific_event_url_name = 'event_details'

        # Credentials
        self.username = 'voltes_v'
        self.email = 'mark@mail.com'
        self.password = 'japanes3_anime145$'

        # Creates a user
        User.objects.create_user(
            username=self.username, email=self.email, password=self.password
            )

        # User Login
        self.client.post(self.login_url, {
            'login': self.username, 'password': self.password
            })

        # Create an Event
        self.test_event = Event.objects.create(
            title='The Greatest Showman in Concert',
            slug='the-greatest-showman',
            blurb='Experience the Greatest Show on Stage',
            event_date=date.today() + timedelta(days=30),
            event_time=time(19, 0),
            post_content='Test event details here',
            author='Mark G',
            entered_by=User.objects.filter(username=self.username).first(),
            status=1)

    def test_new_created_event(self):
        """
        Tests the successful creation of new events
        """
        self.assertEqual(
            self.test_event.title, 'The Greatest Showman in Concert'
            )
        self.assertEqual(self.test_event.slug, 'the-greatest-showman')

    def test_event_details_page(self):
        """
        Tests the rendering of the specific event page with contents
        """
        response = self.client.get(reverse(self.specific_event_url_name,
                                   kwargs={'slug': self.test_event.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('events/event_details.html')
        self.assertContains(response, 'The Goodwill Events presents')

    def test_event_like(self):
        """
        Tests the LIKES for the event
        """
        response = self.client.post(reverse(
            'event_like', kwargs={'slug': self.test_event.slug}))
        user = User.objects.get(username=self.username)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response, reverse('event_details', args=[self.test_event.slug]))
        self.assertTrue(Event.objects.filter(likes=user).exists())

    def test_event_comment(self):
        """
        Tests the posting of comment to the event's page
        """
        self.client.post(reverse(
            'event_comment', kwargs={'slug': self.test_event.slug}), {
                'text_comment': 'This is a comment that I am posting.'
            })
        response = self.client.get(reverse(self.specific_event_url_name,
                                   kwargs={'slug': self.test_event.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Comment.objects.filter(author__username=self.username))
        self.assertContains(response, 'This is a comment that I am posting.')
