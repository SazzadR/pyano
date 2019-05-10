import graphene
from graphene_django.types import DjangoObjectType

from server.authors.models import Author
from server.books.schema import BookType


class AuthorType(DjangoObjectType):
    books = graphene.List(BookType)

    class Meta:
        model = Author
        exclude_fields = ('book_set',)

    def resolve_books(self, info, **kwargs):
        return self.book_set.all()


class Query(object):
    all_authors = graphene.List(AuthorType)

    author = graphene.Field(AuthorType,
                            id=graphene.Int())

    def resolve_all_authors(self, info, **kwargs):
        return Author.objects.all()

    def resolve_author(self, info, **kwargs):
        author_id = kwargs.get('id')

        if author_id is None:
            return None
        else:
            try:
                return Author.objects.get(pk=author_id)
            except Exception:
                return None
