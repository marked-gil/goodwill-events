from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.views import View
from django.contrib.auth.models import User
from seating.models import EventSeating


class MemberAccount(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    Renders the member's account profile and allows their update by the user.
    """
    model = User
    fields = ['first_name', 'last_name', 'email']
    template_name = 'member/member-account.html'
    slug_field = 'username'
    context_object_name = 'member'
    success_message = "You have successfully updated your account."

    def get_context_data(self, **kwargs):
        """
        Insert the single object into the context dict.
        """
        context = {}
        context['event_reservations'] = EventSeating.objects.filter(
            reserved_by=self.request.user)
        return super().get_context_data(**context)

    def get_success_url(self):
        return reverse('member_account', kwargs={'slug': self.kwargs['slug']})

    def get_form(self, form_class=None):
        """
        Set the specified fields as required
        (Idea taken from StockOverflow - See Credits Section in README.)
        """
        form = super(MemberAccount, self).get_form(form_class)
        form.fields['first_name'].required = True
        form.fields['last_name'].required = True
        form.fields['email'].required = True
        return form

    def form_invalid(self, form):
        """
        Shows error message and reloads the page if a form field is left empty.
        """
        messages.error(self.request,
                       'Account cannot be updated with an empty field.')
        return redirect(
            reverse('member_account', kwargs={'slug': self.kwargs['slug']})
            )

    def post(self, request, *args, **kwargs):
        """
        Checks if the updated email address provided already exists before
        submitting to the database.
        """
        self.object = self.get_object()

        current_user = User.objects.filter(id=request.user.id).first()
        found_user = User.objects.filter(
            email=request.POST.get('email')).first()
        if found_user and found_user != current_user:
            messages.error(request, "A similar email address already exists.")
            return redirect(request.path_info)

        return super(MemberAccount, self).post(request, *args, **kwargs)


def error_404_view(request, exception):
    """
    Renders the 404 template when 404 error is raised
    """
    return render(request, '404.html')
