from django.views import View
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.forms import RegistrationForm
from django.contrib.auth import authenticate, login
from tango.decorators import unauthenticated_required


class Register(View):
    @unauthenticated_required()
    def get(self, request):
        form = RegistrationForm()

        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:login'))
        else:
            return render(request, 'accounts/register.html', {'form': form})
