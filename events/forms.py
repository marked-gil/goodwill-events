from django.forms import ModelForm
from .models import Comment


class CommentForm(ModelForm):
    """
    A form class for Comment model with a field for text_comment.
    """
    class Meta:
        model = Comment
        fields = ['text_comment']
