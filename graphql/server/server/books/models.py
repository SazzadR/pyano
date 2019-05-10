from django.db import models

from server.authors.models import Author


class Book(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
