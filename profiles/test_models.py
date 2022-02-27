from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Users


class TestProfilesModels(TestCase):
    """
    Test profile models
    """
    def setUp(self):
        """
        Create mock user
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username='testo',
            password='testingxyd',
        )
        self.client.login(username='testo',
                          password='testingxyd')

    def test_profiles_model(self):
        """
        test the user profile
        """
        self.client.login(username='testo',
                          password='tetsingxyd')
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)

    def test_profiles_model(self):
        """
        test the user profile template
        """
        self.client.login(username='testo',
                          password='tetsingxyd')
        response = self.client.get('/profiles/')
        self.assertTemplateUsed(response, 'profiles/profiles.html')
