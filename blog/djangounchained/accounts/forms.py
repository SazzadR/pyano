from django import forms
from accounts.models import User, Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'username',
            'placeholder': 'Username'
        }
    ))
    first_name = forms.CharField(
        label="First Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'first_name',
                'placeholder': 'First name'
            }
        )
    )
    last_name = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'last_name',
                'placeholder': 'Last name'
            }
        )
    )
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'email',
            'placeholder': 'Email'
        }
    ))
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'password1',
                'placeholder': 'Password'
            }
        )
    )
    password2 = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'password2',
                'placeholder': 'Confirm password'
            }
        )
    )

    field_order = [
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2'
    ]

    class Meta:
        model = get_user_model()
        fields = {
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'username',
            'placeholder': 'Username'
        }
    ))
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'password',
                'placeholder': 'Password'
            }
        )
    )

    field_order = [
        'username',
        'password',
    ]

    class Meta:
        model = get_user_model()
        fields = {
            'username',
            'password',
        }


class UserForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('username', 'email')
        labels = {
            'username': 'Username',
            'email': 'Email'
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'autofocus': True
                }
            )
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        labels = {
            'image': 'Profile image'
        }
