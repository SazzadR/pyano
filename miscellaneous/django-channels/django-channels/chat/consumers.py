import json
import asyncio
from channels.db import DatabaseSyncToAsync
from channels.consumer import AsyncConsumer
from django.contrib.auth import get_user_model
from loguru import logger

from .models import Thread, ChatMessage


class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({
            'type': 'websocket.accept'
        })

        # current_username = self.scope
        other_username = self.scope['url_route']['kwargs']['username']
        logger.debug(self.scope)


    async def websocket_receive(self, event):
        print('receive', event)

    async def websocket_disconnect(self, event):
        print('disconnect', event)
