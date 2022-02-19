from django import forms
from .models import Topic, Blog, Comments


class BlogForm(forms.ModelForm):
    """ Create a form using the blog model fields. """

    class Meta:
        model = Blog
        exclude = ('slug', 'user',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CommentsForm(forms.ModelForm):
    """ 
    Create comments form using the comments
    model 
    """
    class Meta:
        model = Comments
        fields = ['comment',]


