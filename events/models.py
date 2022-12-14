from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import uuid


class Event(models.Model):
    """
    Model for the Event's table in the database
    """
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
        """
        Organizes the objects in the Event's database table according to the
        events' dates in descending order
        """
        ordering = ['-event_date']

    def __str__(self):
        """
        Returns the title of the class Event's instance
        """
        return self.title

    def total_likes(self):
        """
        Returns the number of likes for the class Event's instance
        """
        return self.likes.count()


class Comment(models.Model):
    """
    Model for the Comment's table in the database
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text_comment = models.TextField(max_length=250, blank=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False,
        related_name='event_comments')
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, blank=False, related_name='comments')
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Organizes the objects in the Comment's database table according to
        their 'posted_on' dates in descending order
        """
        ordering = ['-posted_on']

    def __str__(self):
        """
        Returns the specified string for the class Event's instance
        """
        return f'{self.author} commented on {self.event.title} - \
            {self.posted_on.strftime("%Y-%m-%d, %H:%M")}'
