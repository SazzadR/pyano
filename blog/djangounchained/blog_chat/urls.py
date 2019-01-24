from django.urls import path
from .views import ChatHomeView

app_name = 'blog_chat'

urlpatterns = [
    path('', ChatHomeView.as_view(), name='home')
]
