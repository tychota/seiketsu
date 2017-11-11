# cookbook/ingredients/schema.py
import graphene
from graphene_django_extras import DjangoObjectField, DjangoFilterPaginateListField, LimitOffsetGraphqlPagination

from .types import UserType
from .mutations import UserSerializerMutation
from .subscriptions import UserSubscription


class Query(graphene.ObjectType):
    user = DjangoObjectField(UserType, description='Single User query')
    all_users = DjangoFilterPaginateListField(UserType, pagination=LimitOffsetGraphqlPagination())


class Mutation(graphene.ObjectType):
    user_create = UserSerializerMutation.CreateField()
    user_delete = UserSerializerMutation.DeleteField()
    user_update = UserSerializerMutation.UpdateField()


class Subscription(graphene.ObjectType):
    user_subscription = UserSubscription.Field()
