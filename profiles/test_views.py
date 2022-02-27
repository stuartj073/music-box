from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.shortcuts import reverse


class TestProfileViews(TestCase):
    """
    Test profile views are working
    """
    def setUp(self):
        """
        Create mock user to test views
        """
        self.client = Client()
        User.objects.create_user(
            username='testo', 
            password='testingxyz1',
        )

    def test_profile_url(self):
        """
        Test the profile url is loading
        """
        self.client.login(username='testo',
                          password='testingxyz1')
        response = self.client.get(reverse('profile'))
        self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
        
    def test_profile_correct_template_used(self):
        """
        Test profile is rendering correct template
        """
        self.client.login(username='testo',
                    password='testingxyz1')
        response = self.client.get(reverse('profile'))

    def test_profile_accessible_by_name(self):
        """
        Test profile can be accessed by name
        """
        self.client.login(username='testo',
                    password='testingxyz1')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
