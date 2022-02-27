from django.test import TestCase, Client
from django.contrib.auth.models import User

from products.models import Product, Category
from decimal import Decimal
from django.urls import reverse
from .views import basket, add_to_basket, edit_basket, remove_from_basket


class TestBasketViews(TestCase):
    """
    Test basket views
    """
    @classmethod
    def setUpTestData(self):
        """
        Set up user so tests can run
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="testobject", password="12345678"
        )
        self.client.login(username="testobject", password="12345678")

    def setUp(self):
        """
        Create product so basket exists
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

        self.quantity = 1

        self.basket = {
            f'{self.product.id}': "2",
        }

    def test_get_basket(self):
        response = self.client.get("/basket/")
        self.assertEqual(response.status_code, 200)
