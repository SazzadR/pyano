from django.http import Http404
from django.shortcuts import render
from django.views.generic.edit import FormMixin
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ComposeForm
from .models import Thread, ChatMessage


class InboxView(LoginRequiredMixin, ListView):
    template_name = 'chat/inbox.html'

    def get_queryset(self):
        return Thread.object.by_user(self.request.user)


class ThreadView(LoginRequiredMixin, FormMixin, DetailView):
    template_name = 'chat/thread.html'
    form_class = ComposeForm
    success_url = './'

    def get_queryset(self):
        return Thread.object.by_user(self.request.user)

    def get_object(self, queryset=None):
        other_username = self.kwargs.get('username')
        obj = Thread.object.get_or_new(self.request.user, other_username)
        if obj is None:
            raise Http404
        return obj

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            self.create_message(form)
            return self.form_valid(form)
        return self.form_invalid(form)

    def create_message(self, form):
        thread = self.object
        user = self.request.user
        message = form.cleaned_data.get('message')
        ChatMessage.objects.create(thread=thread, user=user, message=message)
