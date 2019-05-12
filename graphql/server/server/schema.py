import graphene

import server.books.schema
import server.authors.schema


class Query(server.authors.schema.Query,
            server.books.schema.Query,
            graphene.ObjectType):
    pass


class Mutation(server.authors.schema.Mutation,
               server.books.schema.Mutation,
               graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
