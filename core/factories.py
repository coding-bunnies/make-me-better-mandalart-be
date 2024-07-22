import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory


class AccountFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.Sequence(lambda n: f"test{n}@example.com")
