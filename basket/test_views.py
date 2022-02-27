from django.test import TestCase
from products.models import Product, Category
from .views import basket, add_to_basket, edit_basket, remove_from_basket


class TestViews(TestCase):

    def test_basket_page_url(self):
        """
        Test basket views
        """
    # def test_basket_page_url(self):
    #     response = self.client.get("/basket")
    #     self.assertEqual(response.status_code, 200)

    def test_get_basket(self):
        response = self.client.get("/basket")
        self.assertTemplateUsed(response, 'basket/basket.html')