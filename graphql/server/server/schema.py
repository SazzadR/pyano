import graphene

import server.books.schema
import server.authors.schema


class Query(server.authors.schema.Query,
            server.books.schema.Query,
            graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query)
