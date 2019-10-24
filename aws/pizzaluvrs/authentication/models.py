from django.contrib.auth.models import (
    AbstractUser, UserManager as UserManagerCore
)


class UserManager(UserManagerCore):
    pass


class User(AbstractUser):
    objects = UserManager
