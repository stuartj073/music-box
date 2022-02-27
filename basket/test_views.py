from django.test import TestCase
from products.models import Product, Category
from django.urls import reverse
from .views import basket, add_to_basket, edit_basket, remove_from_basket


class TestBasketViews(TestCase):

    def test_get_basket(self):
        response = self.client.get("/basket/")
        self.assertEqual(response.status_code, 200)

    # def test_basket_uses_correct_template(self):
    #     response = self.client.get("/basket")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'basket/basket.html')