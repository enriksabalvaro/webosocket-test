# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        pass

    # Receive message from WebSocket
    async def receive(self, text_data):
        print("///////////////////////")
        print(text_data)
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print("this is the message *****************")
        print(message)

        await self.send(text_data=json.dumps({
            'message': message
        }))


    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))