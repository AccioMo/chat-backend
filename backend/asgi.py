"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chatapp.routing

settings_module = "backend.settings.production" if 'WEBSITE_HOSTNAME' in os.environ else "backend.settings.development"
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
		URLRouter(
			chatapp.routing.websocket_urlpatterns
		)
	)
})
