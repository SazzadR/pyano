from . import views
from django.urls import path
from django.conf.urls import url

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]
