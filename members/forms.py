from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        required=True, max_length=20, min_length=4, error_messages={
            "required": "Provide a username."
            })
    first_name = forms.CharField(required=True, max_length=20)
    last_name = forms.CharField(required=True, max_length=20)
    email = forms.CharField(required=True, max_length=50)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name",
                  "email", "password1", "password2",)

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
