from django import forms
from .models import ProductReview
from products.models import Category


class ProductReviewForm(forms.ModelForm):
    """ Create form based on productReview model. """

    class Meta:
        model = ProductReview
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
