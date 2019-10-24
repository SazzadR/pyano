from django.views import View
from django.shortcuts import render

from pizza.models import Pizza


class HomeView(View):
    def get(self, request):
        pizzas = Pizza.objects.all()
        return render(request, "home/home.html", {"pizzas": pizzas})
