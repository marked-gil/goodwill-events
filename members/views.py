from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from .forms import SignUpForm


def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You are signed in successfully."))
            next_url = request.GET.get('next')
            if next_url:
                return redirect(request.GET.get('next'))
            else:
                return redirect('featured_events')

        else:
            messages.success(request, (
                "Username and password did not match. Try again!"
                ))
            return redirect('sign_in')

    else:
        return render(request, './members/login.html', {})


def sign_out(request):
    logout(request)
    messages.success(request, ("Your are succesfully signed out."))
    return redirect('/')


class SignUp(SuccessMessageMixin, CreateView):
    model = User
    form_class = SignUpForm
    template_name = "./members/sign_up.html"
    success_url = "/"
    success_message = "Welcome! You are now a member."

    # Automatically logs in after signing up [See ReadMe for credit]
    def form_valid(self, form):
        valid = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get(
            'username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid
