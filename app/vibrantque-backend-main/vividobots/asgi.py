# """
# ASGI config for vividobots project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
# """

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vividobots.settings')

# application = get_asgi_application()

# myproject/asgi.py
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# import routing  # Import your routing configuration

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": routing.application,  # Use your routing configuration here
# })

# E:\Praveen\Vivido\vividobots\vividobots_v1\Backend1\vividobots\asgi.py

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import routing  # Import your routing configuration

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": routing.application,  # Use your routing configuration here
})

