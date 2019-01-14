from django.urls import path
from accounts.views import profile
from accounts.views.profile import Profile
from accounts.views.register import Register
from accounts.views.login import Login, Logout
from accounts.views.password_reset import PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

app_name = 'accounts'

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password/reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('profile/', Profile.as_view(), name='profile'),
    path('profile/<str:username>/image', profile.get_profile_image)
]
