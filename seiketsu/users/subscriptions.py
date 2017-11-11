from graphene_django_subscriptions import Subscription
from .mutations import UserSerializerMutation


class UserSubscription(Subscription):
    class Meta:
        mutation_class = UserSerializerMutation
        stream = 'users'
        description = 'User Subscription'
