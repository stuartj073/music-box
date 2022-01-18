from django import forms
from .models import Topic, Blog


class BlogForm(forms.ModelForm):
    """ Create a form using the blog model fields. """

    class Meta:
        model = Blog
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        
