from django.test import TestCase
from .forms import ProductForm
from .models import Category


class TestProductForm(TestCase):
    """
    Test product form
    """
    def setUp(self):
        self.category = Category.objects.create(
            name='album',
            friendly_name='albums',
        )

    def test_empty_form(self):
        """
        Test empty form submission
        """
        form = ProductForm({})
        self.assertFalse(form.is_valid())

    def test_form_not_valid_without_name(self):
        """
        Test form without name requirement
        """
        form = ProductForm({
            'category': self.category,
            'description': 'Testing product',
            'price': 2.00
        })
