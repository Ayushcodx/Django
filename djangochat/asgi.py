import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.apps import apps  # Add this import
from django.conf import settings  # Add this import

# Load the Django app configurations
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
