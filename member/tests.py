from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class BaseTestCase(TestCase):
    """
    Customized TestCase
    """
    def setUp(self):
        """ Sets up necessary variables used in testing """
        self.register_url = "/accounts/signup/"
        self.login_url = '/accounts/login/'
        self.logout_url = '/accounts/logout/'
        self.member_account_url_name = 'member_account'

        self.username = 'voltes_v'
        self.first_name = 'Mark'
        self.last_name = 'Dacutan'
        self.email = 'mark@mail.com'
        self.password = 'japanes3_anime145$'


class TestRegistration(BaseTestCase):
    """
    Tests the Register Page
    """
    def test_register_page(self):
        """ Tests the correct rendering of the Register page """
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/signup.html")
        self.assertContains(response, 'Sign Up')

    def test_register_user(self):
        """ Tests user signup on the Register page """
        response = self.client.post(
            self.register_url, {
                'username': self.username,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
                'password1': self.password,
                'password2': self.password,
                }
            )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('featured_events'))

    def test_too_common_password(self):
        """ Tests signup response to very common passwords """
        response = self.client.post(
            self.register_url, {
                'username': self.username,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
                'password1': 12345678,
                'password2': 12345678,
                }
            )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'This password is too common.')

    def test_invalid_email(self):
        """ Tests signup response to invalid email """
        response = self.client.post(
            self.register_url, {
                'username': self.username,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'email': 'anime@',
                'password1': self.password,
                'password2': self.password,
                }
            )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Enter a valid email address.')


class TestLogin(BaseTestCase):
    """
    Tests the Login Page
    """
    def setUp(self):
        """ Sets up the necessary variables used for testing """
        super().setUp()

        User.objects.create_user(
            username=self.username, email=self.email, password=self.password
            )

    def test_login_page(self):
        """ Tests the rendering of the Login page """
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/login.html")
        self.assertContains(response, 'Sign In')

    def test_user_login(self):
        """ Tests the user login """
        response = self.client.post(self.login_url, {
            'login': self.username, 'password': self.password
            })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('featured_events'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_incorrect_login_password(self):
        response = self.client.post(self.login_url, {
            'login': self.username, 'password': 'wrongpasswoRD154'
            })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The username and/or password you ' +
                            'specified are not correct.')

    def test_user_logout(self):
        """ Tests user logout """
        # User Login
        response = self.client.post(self.login_url, {
            'login': self.username, 'password': self.password
            })
        self.assertTrue('_auth_user_id' in self.client.session)

        # User Logout
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse('_auth_user_id' in self.client.session)


class TestMemberAccount(BaseTestCase):
    """
    Tests the Member Account Page
    """
    def setUp(self):
        """ Sets up the necessary variables used for testing """
        super().setUp()

        User.objects.create_user(
            username=self.username, email=self.email, password=self.password
            )

    def test_member_account_page(self):
        """ Tests the rendering of the Member Account page"""
        # User Login
        response = self.client.post(self.login_url, {
            'login': self.username, 'password': self.password
            })
        self.assertTrue('_auth_user_id' in self.client.session)

        # Check Rendering of Member Account page
        response = self.client.get(reverse(
            self.member_account_url_name, kwargs={'slug': self.username}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "member/member-account.html")
        self.assertContains(response, 'Member Account')
