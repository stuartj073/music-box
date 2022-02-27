from django.test import TestCase
from .models import Blog, Comments, Topic


class TestBlogModels(TestCase):
    """
    Test blog models
    """
    def setUp(self):
        """
        Create test blog
        """
        self.blog = Comments.objects.create(
            title='Test Blog',
            topic='Album',
            description = 'Testingalbum',
        )

    def test_blog_string(self):
        self.assertEqual(str(self.blog), 'Test Blog')
