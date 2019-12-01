from topping.models import Topping
from rest_framework import serializers


class ToppingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ["name", "order", "image"]


class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ["id", "name", "order", "image"]
