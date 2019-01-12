from django.contrib.auth.hashers import make_password
from faker import Faker

from accounts.models import User
from blog.models import Post


class UsersSeeder:
    @staticmethod
    def run():
        fake = Faker()
        for _ in range(10):
            user = User.objects.create(
                username=fake.user_name(),
                password=make_password('123456'),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email()
            )

            for _ in range(5):
                Post.objects.create(
                    title=fake.sentence(),
                    content=fake.paragraph(),
                    author=user
                )
