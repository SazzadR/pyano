import graphene


class BookType(graphene.ObjectType):
    name = 'Book'
    description = '...'

    id = graphene.ID()
    title = graphene.String()
    genre = graphene.String()
    author_id = graphene.Int()


# dummy data
books = [
    BookType(id='1', title='Name of the Wind', genre='Fantasy', author_id='1'),
    BookType(id='2', title='The Final Empire', genre='Fantasy', author_id='2'),
    BookType(id='3', title='The Long Earth', genre='Sci-Fi', author_id='3'),
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
