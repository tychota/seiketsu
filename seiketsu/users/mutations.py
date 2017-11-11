from graphene_django_extras import DjangoSerializerMutation
from .serializers import UserSerializer


class UserSerializerMutation(DjangoSerializerMutation):
    class Meta:
        description = " DRF serializer based Mutation for Users "
        serializer_class = UserSerializer
