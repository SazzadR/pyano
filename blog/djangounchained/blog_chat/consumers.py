import json
from datetime import datetime
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, code):
        super().disconnect(code)

    def receive(self, text_data=None, bytes_data=None):
        super().receive(text_data, bytes_data)

        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'sender': self.scope['user'].username,
            'message': message,
            'date_string': f'{datetime.now():%H:%M %p | %B %m}'
        }))
