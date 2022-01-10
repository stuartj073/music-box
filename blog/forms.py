from django import forms 
from .widgets import CustomClearableFileInput
from .models import Product, Category

class BlogForm(models.ModelForm):
    """ Create a form using the blog model fields. """

    class Meta:
        model = Blog
        field = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        topics = Topic.objects.all()
        friendly_names = [(t.id, t.get_friendly_name()) for t in topics]