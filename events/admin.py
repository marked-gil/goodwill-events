from django.contrib import admin
from .models import Event, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    summernote_fields = ('post_content',)
    prepopulated_fields = {"slug": ("title", "event_date",)}
    list_display = ('title', 'event_date', 'event_time',
                    'total_likes', 'status',)
    search_fields = ['title', 'event_date']
    list_filter = ('status', 'event_date',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text_comment', 'event', 'posted_on',)
    list_filter = ('event', 'posted_on')
    search_fields = ['author', 'event', 'text_comment']
