from django.db import models


class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=5)
    summary = models.TextField(default='this is cool!')
