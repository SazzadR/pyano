import graphene

import server.books.schema
import server.authors.schema


class Query(server.books.schema.QueryType,
            server.authors.schema.QueryType,
            graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query)
