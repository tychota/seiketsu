from .models import User
from graphene_django_extras import DjangoInputObjectType


class UserInputType(DjangoInputObjectType):
    class Meta:
        description = " User InputType definition to use as input on an Arguments class on traditional Mutations "
        model = User
