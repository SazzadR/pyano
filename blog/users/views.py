from django.core import mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.views import LoginView as LoginViewCore

from .forms import UserCreationForm


class LoginView(LoginViewCore):
    template_name = 'users/login.html'


class SignupView(CreateView):
    template_name = 'users/register.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        self.send_confirmation_email(user)
        return HttpResponse()
        return HttpResponseRedirect(self.get_success_url())

    def send_confirmation_email(self, user):
        # connection = mail.get_connection()
        # email = mail.EmailMessage(
        #     'Activate your Blog account',
        #     'Body',
        #     'admin@example.com',
        #     [form.cleaned_data['email']],
        #     connection=connection
        # )
        # email.send()

        message = render_to_string('users/account_activation_email.html', {
            'user': user,
            'domain': get_current_site(self.request).domain,
            'uid': user.pk,
        })
        print(message)
