from PIL import Image
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta(object):
        unique_together = ['email']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default=None, upload_to='profile_pics', null=True)

    def __str__(self):
        return '{} Profile'.format(self.user)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
