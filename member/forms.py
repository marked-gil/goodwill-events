from django import forms
from allauth.account.forms import SignupForm, PasswordField
from allauth.account import app_settings
from allauth.utils import set_form_field_order
from django.utils.translation import gettext, gettext_lazy as _, pgettext


class EventsSignUpForm(SignupForm):
    """
    Modifies the django-allauth SignupForm to include first name and last name
    """

    field_order = [
        "username",
        "first_name",
        "last_name",
        "email",
        "password1",
        "password2",
    ]

    def __init__(self, *args, **kwargs):
        # Idea taken from Gavin Wiener's website (See Credit section in README)
        super(EventsSignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'] = forms.CharField(
            required=True, max_length=20, widget=forms.TextInput(
                attrs={"placeholder": ("First Name")}),
                )
        self.fields['last_name'] = forms.CharField(
            required=True, max_length=20, widget=forms.TextInput(
                attrs={"placeholder": ("Last Name")}),
                )
        self.fields["password1"] = PasswordField(
            label=_("Password"), autocomplete="new-password"
        )
        if app_settings.SIGNUP_PASSWORD_ENTER_TWICE:
            self.fields["password2"] = PasswordField(
                label=_("Password (again)"), autocomplete="new-password"
            )

        if hasattr(self, "field_order"):
            set_form_field_order(self, self.field_order)

    def save(self, request):
        user = super(EventsSignUpForm, self).save(request)

        return user
