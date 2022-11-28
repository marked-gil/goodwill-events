from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views import View
from django.contrib.auth.models import User


class MemberAccount(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'member/member-account.html'
    slug_field = 'username'
    context_object_name = 'member'
    success_message = "You have successfully updated your account."

    def get_success_url(self):
        return reverse('member_account', kwargs={'slug': self.kwargs['slug']})


def error_404_view(request, exception):
    """
    Renders the 404 template when 404 error is raised
    """
    return render(request, '404.html')
