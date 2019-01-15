from __future__ import absolute_import, unicode_literals
import os
import glob
from pathlib import Path
from celery import shared_task
from django.conf import settings
from django.contrib.auth.forms import PasswordResetForm
from accounts.models import Profile as ProfileModel, User


@shared_task
def clear_unused_profile_images():
    profile_pictures_directory = settings.MEDIA_ROOT + '/profile_pics/'

    profiles = list(ProfileModel.objects.values('image').values_list('image', flat=True))
    profile_pictures = []
    for profile in profiles:
        profile_pictures.append(Path(profile).name)

    stored_files = glob.glob(f'{profile_pictures_directory}/*')
    stored_profile_pictures = []
    for file in stored_files:
        stored_profile_pictures.append(Path(file).name)

    for stored_profile_picture in stored_profile_pictures:
        if stored_profile_picture not in profile_pictures:
            os.remove(f'{profile_pictures_directory}{stored_profile_picture}')


@shared_task
def send_mail(subject_template_name, email_template_name, context,
              from_email, to_email, html_email_template_name):
    context['user'] = User.objects.get(pk=context['user'])

    PasswordResetForm.send_mail(
        None,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name
    )
