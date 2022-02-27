from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.messages import get_messages

from django.contrib.auth.models import User
from .models import ProductReview
from products.models import Product, Category


class TestProductViews(TestCase):
    """
    Test product views
    """
    def setUp(self):
        """
        Create mock review
        """
        self.admin = User.objects.create(
            username='admin',
            password='test1ing123',
        )
        self.client.force_login(self.admin)

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
            user=self.admin,
            description='testing 12345',
            title='test',
        )

    def test_reviews_page_url(self):
        """
        Test product url
        """
        response = self.client.get(f'/reviews/product_reviews/\n'
                                   f'{self.review.id}/')
        self.assertEqual(response.status_code, 200)

    # def test_products_page_uses_correct_template(self):
    #     """
    #     Test the correct template appears
    #     """
    #     response = self.client.get(reverse('products'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'products/products.html')