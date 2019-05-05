import graphene


def get_book_type():
    from server.books.schema import BookType
    return BookType


def get_books():
    from server.books.schema import books
    return books


class AuthorType(graphene.ObjectType):
    name = 'Author'
    description = '...'

    id = graphene.ID()
    author_name = graphene.String()
    age = graphene.Int()
    books = graphene.List(get_book_type)

    def resolve_books(self, info, **kwargs):
        response = []
        books = get_books()
        for book in books:
            if self.id == book.author:
                response.append(book)

        return response


# dummy data
authors = [
    AuthorType(id='1', author_name='Patrick Rothfuss', age=44),
    AuthorType(id='2', author_name='Brandon Sanderson', age=42),
    AuthorType(id='3', author_name='Terry Pratchett', age=66),
]


class QueryType(graphene.ObjectType):
    name = 'Query'
    description = '...'

    author = graphene.Field(
        AuthorType,
        id=graphene.ID()
    )

    def resolve_author(self, info, **kwargs):
        author_id = kwargs.get('id')

        if author_id is None:
            return None
        else:
            for author in authors:
                if author.id == author_id:
                    return author
