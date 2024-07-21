import random
from datetime import timedelta

import factory
from factory.django import DjangoModelFactory

from checker_board.models import Board


class BoardFactory(DjangoModelFactory):
    class Meta:
        model = Board

    title = factory.Faker("name")
    start_at = factory.Faker("date_this_decade")
    end_at = factory.LazyAttribute(
        lambda o: o.start_at + timedelta(days=random.randint(1, 365))
    )
    user = factory.SubFactory("auth_system.factories.AccountFactory")
