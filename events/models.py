from django.db import models
import uuid
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Event(models.Model):
    STATUS = ((0, "Expired"), (1, "Active"), (2, "Draft"))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=150, blank=False)
    slug = models.SlugField(max_length=150, blank=False)
    blurb = models.CharField(max_length=200, blank=False)
    event_date = models.DateField(unique=True, blank=False)
    event_time = models.TimeField(blank=False)
    post_content = models.TextField(blank=False)
    featured_image = CloudinaryField('image', default='proxy_image')
    author = models.CharField(max_length=150)
    entered_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='event_post')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, blank=True, related_name='event_likes')
    status = models.IntegerField(choices=STATUS, default=2)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()
