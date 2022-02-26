from django.test import TestCase


class TestCheckoutViews(TestCase):
    """
    Test the url of the checkout
    page works
    """

    def test_get_checkout(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

