from django import forms
from allauth.account.forms import SignupForm


class EventsSignUpForm(SignupForm):
    """
    Modifies the django-allauth SignupForm
    """
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

    def save(self, request):
        user = super(EventsSignUpForm, self).save(request)

        return user
