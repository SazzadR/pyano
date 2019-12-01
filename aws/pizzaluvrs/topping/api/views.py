from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView
)

from topping.models import Topping
from .serializers import ToppingCreateSerializer, ToppingSerializer


class ToppingsCreateView(CreateAPIView):
    serializer_class = ToppingCreateSerializer


class ToppingsListView(ListAPIView):
    queryset = Topping.objects.all().order_by("order")
    serializer_class = ToppingSerializer


class ToppingsDetailView(RetrieveAPIView):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer
