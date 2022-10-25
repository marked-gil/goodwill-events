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


class EventSeating(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='seats')
    seat_location = models.ForeignKey(
        VenueSeat, on_delete=models.CASCADE, related_name='event_seating')
    reserved_on = models.DateTimeField(auto_now_add=True)
    reserved_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='event_seats')

    class Meta:
        ordering = ['-reserved_on']
        unique_together = [['event', 'seat_location']]

    def __str__(self):
        return f"{self.event.title} on {self.event.event_date}"
