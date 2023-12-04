# asgi.py

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from room import routing  # Move the import here

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        routing.websocket_urlpatterns
    ),
})

from uvicorn.workers import UvicornWorker
application = UvicornWorker(application)
