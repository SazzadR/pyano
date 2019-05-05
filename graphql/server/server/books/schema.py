import graphene

from server.authors.schema import AuthorType, authors


class BookType(graphene.ObjectType):
    name = 'Book'
    description = '...'

    id = graphene.ID()
    title = graphene.String()
    genre = graphene.String()
    author = graphene.Field(AuthorType)

    def resolve_author(self, info, **kwargs):
        for author in authors:
            if self.author == author.id:
                return author


# dummy data
books = [
    BookType(id='1', title='Name of the Wind', genre='Fantasy', author='1'),
    BookType(id='2', title='The Final Empire', genre='Fantasy', author='2'),
    BookType(id='3', title='The Long Earth', genre='Sci-Fi', author='3'),
]


class QueryType(graphene.ObjectType):
    name = 'Query'
    description = '...'

    book = graphene.Field(
        BookType,
        id=graphene.ID()
    )

    def resolve_book(self, info, **kwargs):
        book_id = kwargs.get('id')

        if book_id is None:
            return None
        else:
            for book in books:
                if book.id == book_id:
                    return book
