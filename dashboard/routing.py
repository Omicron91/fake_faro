from django.urls import path
from .consumers import FakeFaroConsumer


ws_urlpatterns = [
    path("ws/fake_faro_data/", FakeFaroConsumer.as_asgi())
]