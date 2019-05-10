from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.author_name
