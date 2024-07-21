from django.db import models
from django_extensions.db.models import TimeStampedModel

from core.models import TimeStamped


# Create your models here.
class Board(TimeStamped):
    title = models.CharField(max_length=16)
    user = models.ForeignKey(
        "auth_system.Account",
        on_delete=models.CASCADE,
        related_name="boards",
    )
    achievement = models.PositiveIntegerField(default=0)
    start_at = models.DateField()
    end_at = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "board"
        verbose_name = "Board"
        verbose_name_plural = "Boards"


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


class Cycle(models.TextChoices):
    ONCE = "once", "Once"
    DAILY = "daily", "Daily"
    WEEKLY = "weekly", "Weekly"
    MONTHLY = "monthly", "Monthly"
    YEARLY = "yearly", "Yearly"


class Action(TimeStamped):
    title = models.CharField(max_length=16)
    mission = models.ForeignKey(
        Mission,
        on_delete=models.CASCADE,
        related_name="actions",
    )
    completed_at = models.DateTimeField(blank=True, null=True)
    cycle = models.CharField(max_length=16, choices=Cycle.choices)
    goal_unit = models.PositiveIntegerField()
    action_unit = models.PositiveIntegerField()
    current_unit = models.PositiveIntegerField(default=0)
    achievement = models.PositiveIntegerField(default=0)
    unit_name = models.CharField(max_length=8)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "action"
        verbose_name = "Action"
        verbose_name_plural = "Actions"

    def increase_achievement(self):
        self.current_unit += self.action_unit
        self.achievement = self.current_unit / self.goal_unit * 100
        return self.save()
