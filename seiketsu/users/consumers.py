from graphene_django_subscriptions import GraphqlAPIDemultiplexer
from .subscriptions import UserSubscription


class UsersDemultiplexer(GraphqlAPIDemultiplexer):
    consumers = {
      'users': UserSubscription.get_binding().consumer,
    }
