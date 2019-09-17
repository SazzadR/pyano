from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UsernameField
from django.contrib.auth.forms import (
    UserCreationForm as UserCreationFormCore,
    AuthenticationForm as AuthenticationFormCore
)


class UserCreationForm(UserCreationFormCore):
    class Meta:
        model = get_user_model()
        fields = ("username",)
        field_classes = {"username": UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm password"


class AuthenticationForm(AuthenticationFormCore):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "Username"
        self.fields["password"].widget.attrs["placeholder"] = "Password"
