from django.db import models
from django_extensions.db.models import TimeStampedModel


# Create your models here.
class TimeStamped(TimeStampedModel):
    deleted = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        abstract = True
