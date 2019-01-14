from django.urls import reverse_lazy
from accounts.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.views import PasswordResetView as PasswordResetViewCore, \
    PasswordResetDoneView as PasswordResetDoneViewCore, \
    PasswordResetConfirmView as PasswordResetConfirmViewCore, \
    PasswordResetCompleteView as PasswordResetCompleteViewCore


class PasswordResetView(PasswordResetViewCore):
    email_template_name = 'accounts/password_reset_email.html'
    template_name = 'accounts/password_reset_form.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('accounts:password_reset_done')


class PasswordResetDoneView(PasswordResetDoneViewCore):
    template_name = 'accounts/password_reset_done.html'


class PasswordResetConfirmView(PasswordResetConfirmViewCore):
    form_class = SetPasswordForm
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class PasswordResetCompleteView(PasswordResetCompleteViewCore):
    template_name = 'accounts/password_reset_complete.html'
