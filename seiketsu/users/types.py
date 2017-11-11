from .models import User
from graphene_django import DjangoObjectType
from graphene_django_extras import DjangoListObjectType, DjangoSerializerType
from graphene_django_extras.paginations import LimitOffsetGraphqlPagination

from .serializers import UserSerializer


class UserType(DjangoObjectType):
    class Meta:
        model = User
        description = " Type definition for a single user "
        filter_fields = {
            'id': ['exact', ],
            'first_name': ['icontains', 'iexact'],
            'last_name': ['icontains', 'iexact'],
            'username': ['icontains', 'iexact'],
            'email': ['icontains', 'iexact']
        }


class UserListType(DjangoListObjectType):
    class Meta:
        description = " Type definition for user list "
        model = User
        pagination = LimitOffsetGraphqlPagination(max_limit=20)


class UserModelType(DjangoSerializerType):
    class Meta:
        description = " User's model type definition "
        serializer_class = UserSerializer
        pagination = LimitOffsetGraphqlPagination(default_limit=25)
        filter_fields = {
            'id': ['exact', ],
            'first_name': ['icontains', 'iexact'],
            'last_name': ['icontains', 'iexact'],
            'username': ['icontains', 'iexact'],
            'email': ['icontains', 'iexact'],
            'is_staff': ['exact']
        }
