import graphene
from graphene_django.types import DjangoObjectType

from server.books.models import Book


class BookType(DjangoObjectType):
    class Meta:
        model = Book


class Query(object):
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
