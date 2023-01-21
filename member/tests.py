from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


# Create your tests here.
class BaseTestCase(TestCase):
    def setUp(self):
        self.register_url = "/accounts/signup"
        self.login_url = "/account/login"

        self.mock_user = {
            'username': 'voltes_v',
            'first_name': 'Mark',
            'last_name': 'Dacutan',
            'email': 'voltes_v@mail.com',
            'password1': 'japanese_anime145',
            'password2': 'japanese_anime145',
        }

        return super().setUp()


class TestAuthentication(BaseTestCase):

    def test_register_page(self):
        response = self.client.get(self.register_url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/signup.html")
        self.assertContains(response, 'Sign Up')

    def test_register_user(self):
        response = self.client.post(
            self.register_url, self.mock_user, follow=True
            )
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get(self.login_url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/login.html")
        self.assertContains(response, 'Sign In')

    def test_login_user(self):
        response = self.client.post(
            self.login_url, self.mock_user, follow=True
            )
        self.assertEqual(response.status_code, 200)


