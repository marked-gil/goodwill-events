from django.db import models
from django.contrib.auth.models import User
from events.models import Event
import uuid


class VenueSeat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    seat_location = models.CharField(max_length=10, unique=True, blank=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['seat_location']

    def __str__(self):
        return self.seat_location
