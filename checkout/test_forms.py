from django.test import TestCase
from .forms import OrderForm


class TestCheckoutForms(TestCase):
    """
    Test checkout form is working
    """

    def test_empty_checkout_form(self):
        """
        Test name form is required
        """

        form = OrderForm({
            'first_name': '',
            'surname': 'testo',
            'email': 'test@gmail.com',
            'phone_number': '12345678',
            'street_address1': 'Test',
            'street_address2': 'Testo',
            'town_or_city': 'dub',
            'country': 'dubo',
            'postcode': 'testx67',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(
            form.errors['first_name'][0], 'This field is required.')

    def test_surname_is_required(self):
        """
        Test surname  is required
        """

        form = OrderForm({
            'first_name': 'name0',
            'surname': '',
            'email': 'test@gmail.com',
            'phone_number': '12345678',
            'street_address1': 'Test',
            'street_address2': 'Testo',
            'town_or_city': 'dub',
            'country': 'dubo',
            'postcode': 'testx67',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('surname', form.errors.keys())
        self.assertEqual(
            form.errors['surname'][0], 'This field is required.')

    def test_email_is_required(self):
        """
        Test email is required
        """

        form = OrderForm({
            'first_name': 'name0',
            'surname': 'testing',
            'email': '',
            'phone_number': '12345678',
            'street_address1': 'Test',
            'street_address2': 'Testo',
            'town_or_city': 'dub',
            'country': 'dubo',
            'postcode': 'testx67',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def test_phone_is_required(self):
        """
        Test phone is required
        """

        form = OrderForm({
            'first_name': 'name0',
            'surname': 'testing',
            'email': 'test@gmail.com',
            'phone_number': '',
            'street_address1': 'Test',
            'street_address2': 'Testo',
            'town_or_city': 'dub',
            'country': 'dubo',
            'postcode': 'testx67',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

    def test_street_address_is_required(self):
        """
        Test address is required
        """

        form = OrderForm({
            'first_name': 'name0',
            'surname': 'testing',
            'email': 'test@gmail.com',
            'phone_number': '12345678',
            'street_address1': '',
            'street_address2': 'Testo',
            'town_or_city': 'dub',
            'country': 'dubo',
            'postcode': 'testx67',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')

    def test_town_or_city_is_required(self):
        """
        Test town/city is required
        """

        form = OrderForm({
            'first_name': 'name0',
            'surname': 'testing',
            'email': 'test@gmail.com',
            'phone_number': '12345678',
            'street_address1': 'Test',
            'street_address2': 'Testo',
            'town_or_city': '',
            'country': 'dubo',
            'postcode': 'testx67',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_country_is_required(self):
        """
        Test country is required
        """

        form = OrderForm({
            'first_name': 'name0',
            'surname': 'testing',
            'email': 'test@gmail.com',
            'phone_number': '12345678',
            'street_address1': 'Test',
            'street_address2': 'Testo',
            'town_or_city': 'dub',
            'country': '',
            'postcode': 'd1812345',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(
            form.errors['country'][0], 'This field is required.')
