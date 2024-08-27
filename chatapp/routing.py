from django.urls import re_path
from .consumers import ChatConsumer

websocket_urlpatterns = [
	re_path(r'ws/chat/(?P<chat_id>[a-f0-9-]+)', ChatConsumer.as_asgi()),
    re_path(r'.*', ChatConsumer.as_asgi()),
]
