import json
import asyncio
from channels.db import DatabaseSyncToAsync
from channels.consumer import AsyncConsumer
from django.contrib.auth import get_user_model

from .models import Thread, ChatMessage


class ChatConsumer(AsyncConsumer):
    def websocket_connect(self, event):
        print('connect', event)

    def websocket_receive(self, event):
        print('receive', event)

    def websocket_disconnect(self, event):
        print('disconnect', event)
