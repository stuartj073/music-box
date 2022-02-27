from django.test import TestCase
from .models import Order
from products.model import Product


class TestCheckoutModels(TestCase):
    """
    Test Checkout models
    """
    def test_order_str_method(self):
        """
        Test the order model returns the order no
        """
        order = Order.objects.create(order_number="123456")
        self.assertEqual(str(order), "123456")


# class TestOrderLineModel(self):
#         """
#         Test order line models str method
#         """
#         def test_orderline_str_method(self):
#             product = Product.objects.create(name="test", price=2.00)
#             order = Order.objects.create(order_number="123456")
#             self.assertEqual(str())

