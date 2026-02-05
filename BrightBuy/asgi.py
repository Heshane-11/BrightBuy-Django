import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import orders.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BrightBuy.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        orders.routing.websocket_urlpatterns
    ),
})
