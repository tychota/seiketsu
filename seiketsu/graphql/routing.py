from channels.routing import route_class
from seiketsu.users.consumers import UsersDemultiplexer


channel_routing = [
    route_class(UsersDemultiplexer)
]
