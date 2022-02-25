from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ 
    Create a form using the fields from the product model
    """

    class Meta:
        model = Product
        exclude = ('sku',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names

