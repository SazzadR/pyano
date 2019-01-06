import base64
from django.views import View
from accounts.models import User
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from accounts.forms import UserForm, ProfileForm
from accounts.tasks import clear_unused_profile_images
from django.core.files.storage import FileSystemStorage


class Profile(View):
    def insert_profile_image(self, request):
        if request.user.profile.image:
            request.user.profile.image_url = request.build_absolute_uri(request.user.profile.image.url)
        else:
            request.user.profile.image_url = 'http://www.gravatar.com/avatar/0bc83cb571cd1c50ba6f3e8a78ef1346'

    def get(self, request):
        self.insert_profile_image(request)
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

        return render(request, 'accounts/profile.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

        if user_form.is_valid():
            user = user_form.save()

            image = request.FILES['image']
            fs = FileSystemStorage(location=settings.MEDIA_ROOT + '/profile_pics')
            uploaded_filename = fs.save(image.name, image)
            user.profile.image = 'profile_pics/{}'.format(uploaded_filename)
            user.profile.save()

        clear_unused_profile_images.delay()

        self.insert_profile_image(request)

        return render(request, 'accounts/profile.html', {
            'user_form': user_form,
            'profile_form': profile_form
        })


def get_profile_image(request, username):
    user = User.objects.get(username=username)

    try:
        with open(user.profile.image.path, 'rb') as img_f:
            encoded_string = base64.b64encode(img_f.read())
            status = 200
    except (ValueError, FileNotFoundError):
        encoded_string = None
        status = 404

    return HttpResponse(encoded_string, status=status)
