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
