from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import PizzaCreateView, PizzaDetailView, PizzaListByUserView

app_name = "pizza"

urlpatterns = [
    path("make/", csrf_exempt(PizzaCreateView.as_view()), name="create"),
    path("<int:pk>/", PizzaDetailView.as_view(), name="show"),
    path("users/<int:pk>/", PizzaListByUserView.as_view(), name="list-by-user"),
]
