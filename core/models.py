from django.db import models
from django_extensions.db.models import TimeStampedModel


# Create your models here.
class TimeStamped(TimeStampedModel):
    deleted = models.DateTimeField(default=None, null=True, blank=True)

    class Meta:
        abstract = True
