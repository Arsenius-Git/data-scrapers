from django.urls import re_path

from app4.mysite.rooms.routing import websocket_urlpatterns
from . import consumers

websocket_urlpatterns = [
    re_path()
]