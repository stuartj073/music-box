from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.messages import get_messages

from django.contrib.auth.models import User
from .models import Category, Product


class TestProductViews(TestCase):
    """
    Test product views
    """
    def setUp(self):
        """
        Create product so basket exists
        """
        self.admin = User.objects.create(
            username='admin',
            password='test1ing123',
            is_superuser=True,
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

    def test_product_page_url(self):
        """
        Test product url
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_products_page_uses_correct_template(self):
        """
        Test the correct template appears
        """
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_products_page_accessible_by_name(self):
        """
        Test products link throughout site
        """
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_product_details(self):
        """
        Test product details view
        """
        response = self.client.get(f'/products/product_details/\n'
                                   f'{self.product.id}/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_accessible_by_name(self):
        """
        Test product detail name link is accessible
        """
        response = self.client.get(reverse('product_detail',
                                   args=f'{self.product.id}'))
        self.assertEqual(response.status_code, 200)

    def test_search_function(self):
        """
        Test the search bar for test product
        """
        response = self.client.get(
            '/products/?', {'q': f'{self.product.name}'}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['search_term'],
                         'product1')
