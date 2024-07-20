import factory
from factory.django import DjangoModelFactory

from auth.models import Account


class AccountFactory(DjangoModelFactory):
    class Meta:
        model = Account

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.Sequence(lambda n: f"test{n}@example.com")
