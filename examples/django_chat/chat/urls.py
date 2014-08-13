
from django.conf.urls import patterns, include, url
import socketio.sdjango


from django.conf.urls.static import static
from django.conf import settings

socketio.sdjango.autodiscover()

urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    patterns("chat.views",
    url("^socket\.io", include(socketio.sdjango.urls)),
    url("^$", "rooms", name="rooms"),
    url("^create/$", "create", name="create"),
    url("^(?P<slug>.*)$", "room", name="room"),
)
