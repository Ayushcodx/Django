import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from room import routing  # Import the 'routing' module

# Load the Django app configurations
from django.apps import apps
from django.conf import settings
apps.populate(settings.INSTALLED_APPS)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        routing.websocket_urlpatterns
    ),
})

from uvicorn.workers import UvicornWorker
application = UvicornWorker(application)
