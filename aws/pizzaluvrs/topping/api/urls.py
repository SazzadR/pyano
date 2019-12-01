from django.urls import path

from .views import ToppingsCreateView, ToppingsListView, ToppingsDetailView

app_name = "api_toppings"

urlpatterns = [
    path('', ToppingsListView.as_view(), name="toppings"),
    path("<int:pk>/", ToppingsDetailView.as_view(), name="show"),
    path("create/", ToppingsCreateView.as_view(), name="create"),
]
