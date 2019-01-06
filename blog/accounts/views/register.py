from django.views import View
from django.urls import reverse
from django.http import HttpResponse
from accounts.forms import RegistrationForm
from django.shortcuts import render, redirect

class Register(View):
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

