from django.urls import reverse
from django.views.generic import View
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView as LoginViewCore

from .forms import UserCreationForm, AuthenticationForm


class LoginView(LoginViewCore):
    form_class = AuthenticationForm
    template_name = "authentication/login.html"

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or reverse("home:home")


class LogoutView(View):
    def get(self, request):
        logout(request=request)
        return redirect("home:home")


class RegistrationView(View):
    form_class = UserCreationForm
    template_name = "authentication/registration.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request=request, user=user)
            return redirect("home:home")
        return render(request, self.template_name, {"form": form})
