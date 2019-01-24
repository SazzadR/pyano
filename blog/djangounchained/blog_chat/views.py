from django.shortcuts import render
from django.views.generic import TemplateView


class ChatHomeView(TemplateView):
    template_name = 'blog_chat/home.html'
