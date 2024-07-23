from decimal import Decimal

from django.db import models
from django_extensions.db.models import TimeStampedModel
from simple_history.models import HistoricalRecords

from core.models import TimeStamped


# Create your models here.
class Board(TimeStamped):
    title = models.CharField(max_length=16)
    user = models.ForeignKey(
        "auth_system.Account",
        on_delete=models.CASCADE,
        related_name="boards",
    )
    daily_goal = models.PositiveIntegerField(help_text="일일 목표치", default=0)
    total_percentage = models.DecimalField(
        help_text="전체 달성률", default=0, max_digits=7, decimal_places=4
    )
    start_at = models.DateField()
    end_at = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "board"
        verbose_name = "Board"
        verbose_name_plural = "Boards"

    def update_total_percentage(self, action):
        total_period = (self.end_at - self.start_at).days
        action_period = action.period.value or 1

        self.total_percentage += Decimal(
            round(
                action.current_unit
                / action.goal_unit
                * action_period
                / total_period
                * 100,
                4,
            )
        )
        self.save()


class Mission(TimeStamped):
    title = models.CharField(max_length=16)
    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        related_name="missions",
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "mission"
        verbose_name = "Mission"
        verbose_name_plural = "Missions"


class Period(models.IntegerChoices):
    ONCE = 0
    DAILY = 1
    WEEKLY = 7
    MONTHLY = 30
    YEARLY = 365


class Action(TimeStamped):
    title = models.CharField(max_length=16)
    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        related_name="actions",
        null=True,
    )
    mission = models.ForeignKey(
        Mission,
        on_delete=models.CASCADE,
        related_name="actions",
    )
    completed_at = models.DateTimeField(blank=True, null=True)
    period = models.CharField(max_length=16, choices=Period.choices)
    goal_unit = models.PositiveIntegerField(help_text="목표치")
    action_unit = models.PositiveIntegerField(help_text="수행 단위")
    current_unit = models.PositiveIntegerField(help_text="실제 수행치", default=0)
    achievement = models.PositiveIntegerField(default=0)
    unit_name = models.CharField(max_length=8)
    position = models.PositiveIntegerField(null=True, blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "action"
        verbose_name = "Action"
        verbose_name_plural = "Actions"
        unique_together = ("board", "position")

    def increase_achievement(self):
        self.current_unit += self.action_unit
        self.achievement = self.current_unit / self.goal_unit * 100
        return self.save()


class DailyStatistics(TimeStamped):
    """중간에 아이템을 하나 삭제하게 되더라도, 기존에 쌓아둔 확률을 유지하기 위해 전체 달성률을 매일 계산하여 저장합니다."""

    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        related_name="statistics",
    )

    goal = models.PositiveIntegerField(help_text="일일 목표치", default=0)
    achievement = models.PositiveIntegerField(help_text="실제 달성 횟수", default=0)
    percentage = models.PositiveIntegerField(help_text="일일 달성률", default=0)

    class Meta:
        db_table = "statistics"
        verbose_name = "Statistics"
        verbose_name_plural = "Statistics"
