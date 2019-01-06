from .models import User, Profile
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    if kwargs.get('created') is True:
        Profile.objects.create(user=kwargs.get('instance'))
