from django.test import TestCase
from .models import ProductReview
from products.models import Product, Category


class TestProductModel(TestCase):
    """
    Test the models in products app
    """
    def setUp(self):
        """
        Make mock product to test models
        """
        self.category = Category.objects.create(
            name='test',
            friendly_name='Test 1',
        )
        self.product = Product.objects.create(
            category=self.category,
            name='product1',
            description='testing 12345',
            condition='mint',
            price=2.00,
            sku='12345',
        )

        self.review = ProductReview.objects.create(
            name=self.product,
            description='testing 12345',
            title='test',
        )

    def test_product_str_method(self):
        """
        Test that category returns string
        """
        self.assertEqual(str(self.review.name), 'product1')

    def test_product_str_method(self):
        """
      Test that category returns string
        """
        self.assertEqual(str(self.review.name), 'product1')
