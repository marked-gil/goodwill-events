from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
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
