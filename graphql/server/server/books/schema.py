import graphene
from graphene_django.types import DjangoObjectType

from server.books.models import Book
from server.authors.models import Author


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)

    book = graphene.Field(BookType,
                          id=graphene.Int())

    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()

    def resolve_book(self, info, **kwargs):
        book_id = kwargs.get('id')

        if book_id is None:
            return None
        else:
            try:
                return Book.objects.get(pk=book_id)
            except Exception:
                return None


class CreateBook(graphene.Mutation):
    # The class attributes define the response of the mutation
    book = graphene.Field(BookType)

    class Arguments:
        title = graphene.String(required=True)
        genre = graphene.String(required=True)
        author_id = graphene.Int(required=True)

    def mutate(self, info, title, genre, author_id):
        book = Book.objects.create(title=title, genre=genre, author=Author.objects.get(pk=author_id))
        return CreateBook(book=book)


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
