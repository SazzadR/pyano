from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as UserCreationFormCore


class UserCreationForm(UserCreationFormCore):
    username = forms.CharField(widget=forms.TextInput())
    first_name = forms.CharField(widget=forms.TextInput(), required=False)
    last_name = forms.CharField(widget=forms.TextInput(), required=False)
    email = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password', strip=False)
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Password confirmation', strip=False)

    field_order = [
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2',
    ]

    class Meta:
        model = get_user_model()
        fields = {
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        }
