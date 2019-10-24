import json
import urllib

from django.views import View
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Pizza
from topping.models import Topping


class PizzaCreateView(LoginRequiredMixin, View):
    def get(self, request):
        toppings = Topping.objects.all().order_by("order")
        return render(request, "pizza/create.html", {"toppings": toppings})

    def post(self, request):
        info = json.loads(request.body)

        image_binary = urllib.request.urlopen(info.get("image"))
        with open("{}/pizza/{}.png".format(settings.MEDIA_ROOT, info.get("name")), "wb") as f:
            f.write(image_binary.file.read())

        pizza = Pizza(name=info.get("name"), image="pizza/{}.png".format(info.get("name")), created_by=request.user)
        pizza.save()
        pizza.toppings.set(info.get("toppings"))

        return HttpResponse(pizza.id)


class PizzaDetailView(LoginRequiredMixin, DetailView):
    model = Pizza
    template_name = "pizza/show.html"


class PizzaListByUserView(LoginRequiredMixin, ListView):
    context_object_name = 'pizzas'
    template_name = "pizza/list.html"

    def get_queryset(self):
        return Pizza.objects.filter(created_by=self.request.user)
