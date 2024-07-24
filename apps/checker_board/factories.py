import random
from datetime import timedelta

import factory
from factory.django import DjangoModelFactory

from apps.checker_board.models import Board, Mission, Action, Period, DailyStatistics


class BoardFactory(DjangoModelFactory):
    class Meta:
        model = Board

    title = factory.Faker("name")
    start_at = factory.Faker("date_this_decade")
    end_at = factory.LazyAttribute(
        lambda o: o.start_at + timedelta(days=random.randint(1, 365))
    )
    user = factory.SubFactory("auth_system.factories.AccountFactory")


class MissionFactory(DjangoModelFactory):
    class Meta:
        model = Mission

    title = factory.Faker("name")
    board = factory.SubFactory(BoardFactory)


class ActionFactory(DjangoModelFactory):
    class Meta:
        model = Action

    title = factory.Faker("name")
    mission = factory.SubFactory(MissionFactory)
    period = factory.Faker("random_element", elements=Period.values)
    completed_at = factory.Faker("date_time_this_decade", tzinfo=None)
    goal_unit = factory.Faker("random_int", min=100, max=1000)
    action_unit = factory.Faker("random_int", min=1, max=10)
    unit_name = factory.Faker("word")


class DailyStatisticsFactory(DjangoModelFactory):
    class Meta:
        model = DailyStatistics

    board = factory.SubFactory(BoardFactory)
    goal = factory.Faker("random_int", min=100, max=1000)
    achievement = factory.Faker("random_int", min=1, max=10)
    percentage = factory.Faker("pyfloat", min_value=0, max_value=100)
    target_date = factory.Faker("date_time_this_decade", tzinfo="Asia/Seoul")
