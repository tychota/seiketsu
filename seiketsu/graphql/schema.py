import graphene

import seiketsu.users.schema


class Query(seiketsu.users.schema.Query, graphene.ObjectType):
    pass


class Mutation(seiketsu.users.schema.Mutation, graphene.ObjectType):
    pass


class Subscription(seiketsu.users.schema.Subscription, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)
