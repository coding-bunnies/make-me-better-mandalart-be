from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.checker_board.models import Action, DailyStatistics


@receiver(post_save, sender=Action)
def update_daily_statistics(sender, **kwargs):
    instance = kwargs.get("instance")

    board = instance.board

    DailyStatistics.objects.update_or_create(
        board=board,
        created_at__date=datetime.today().date(),
        defaults={
            "goal": instance.goal_unit,
            "achievement": instance.current_unit,
            "percentage": instance.achievement,
        },
    )


@receiver(post_save, sender=Action)
def update_total_statistics(sender, **kwargs):
    instance = kwargs.get("instance")
    board = instance.board

    board.update_total_percentage(action=instance)
