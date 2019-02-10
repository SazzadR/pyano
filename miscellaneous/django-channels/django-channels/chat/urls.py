from django.urls import path, re_path

from .views import InboxView, ThreadView

app_name = 'chat'

urlpatterns = [
    path('', InboxView.as_view()),
    path('<str:username>/', ThreadView.as_view()),
]
