from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ Create a form using the fields from the product model. """

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()