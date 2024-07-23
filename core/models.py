from django.db import models
from django_extensions.db.models import TimeStampedModel
from simple_history.models import HistoricalRecords


# Create your models here.
class TimeStamped(TimeStampedModel):
    deleted = models.DateTimeField(default=None, null=True, blank=True)
    history = HistoricalRecords()

    class Meta:
        abstract = True
