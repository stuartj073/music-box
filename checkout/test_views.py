from django.test import TestCase


class TestCheckoutViews(TestCase):
    """
    Test the url of the checkout
    page works
    """
    def test_get_checkout(self):
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

        response = self.client.get("/checkout/")
        self.assertEqual(response.status_code, 302)
