from faker import Faker
from factory import DjangoModelFactory, lazy_attribute

from .models import Product

FAKER = Faker(locale='en_US')


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    title = lazy_attribute(lambda x: FAKER.sentence())
    description = lazy_attribute(lambda x: FAKER.text())
    price = lazy_attribute(lambda x: FAKER.random_number(digits=3))
    summary = lazy_attribute(lambda x: FAKER.text())
    featured = lazy_attribute(lambda x: FAKER.boolean())
