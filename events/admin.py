from django.contrib import admin
from .models import Event, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Event)
class EventAdmin(SummernoteModelAdmin):
    """
    Particularizes the layout and content of the admin interface
    for the Event model
    """
    summernote_fields = ('post_content',)
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'event_date', 'event_time',
                    'total_likes', 'status',)
    search_fields = ['title', 'event_date']
    list_filter = ('status', 'event_date',)

    def get_form(self, request, *args, **kwargs):
        """
        Add the current user as the default value for the 'author'
        and 'entered_by' fields
        """
        form = super(EventAdmin, self).get_form(
            request, *args, **kwargs)
        form.base_fields['author'].initial = request.user
        form.base_fields['entered_by'].initial = request.user
        return form


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Particularizes the layout and content of the admin interface
    for the Comment model
    """
    list_display = ('author', 'text_comment', 'event', 'posted_on',)
    list_filter = ('event', 'posted_on')
    search_fields = ['author', 'event', 'text_comment']
