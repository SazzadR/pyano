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


class Query(graphene.ObjectType):
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


class CreateAuthor(graphene.Mutation):
    # The class attributes define the response of the mutation
    author = graphene.Field(AuthorType)

    class Arguments:
        author_name = graphene.String(required=True)
        age = graphene.Int(required=True)

    def mutate(self, info, author_name, age):
        author = Author.objects.create(author_name=author_name, age=age)
        return CreateAuthor(author=author)


class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
