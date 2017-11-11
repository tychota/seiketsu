# In routing.py
from django.conf import settings

from channels.routing import route, include
from channels.staticfiles import StaticFilesConsumer
from channels.handler import ViewConsumer

from seiketsu.graphql.routing import channel_routing as graphql_routing

channel_routing = [
    include(graphql_routing, path="^/graphql"),
    route("http.request", StaticFilesConsumer()) if settings.DEBUG else route("http.request", ViewConsumer()),
]
