import graphene
import graphene_app.schema

class Query(graphene_app.schema.Query, graphene.ObjectType):
    pass

class Mutation(graphene_app.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)