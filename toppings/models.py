from django.db import models


class Toppings(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(unique=True)
    image = models.ImageField(upload_to="toppings/")

    def __str__(self):
        return self.name
