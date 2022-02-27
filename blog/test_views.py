from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Blog

from django.shortcuts import reverse


class TestBlogViews(TestCase):
    """
    Tests for all blog views
    """
    @classmethod
    def setUpTestData(self):
        """
        Set up data so tests can run
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="testobject", password="12345678"
        )
        self.client.login(username="testobject", password="12345678")

    def test_get_blog_page(self):
        response = self.client.get('/blog/blogs')
        self.assertEqual(response.status_code, 200)

    def test_blogs_uses_correct_template(self):
        response = self.client.get('/blog/blogs')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogs.html')

    def test_blogs_is_accessible_by_name(self):
        response = self.client.get(reverse('blogs'))
        self.assertEqual(response.status_code, 200)

    # def test_post_string_method_returns(self):
    #     blog = Blog.objects.create(title="Test")
    #     self.assertEqual(str(blog), "Test")

    def test_blogs_display(self):
        blogs = Blog.objects.all()
        for blog in blogs:
            response = self.client.get(reverse('blogs'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, blog.id)

    # def test_get_blog_details_page(self):
    #     blog = Blog.objects.create(title='Test')
    #     response = self.client.get(f'blog/blog_details/{blog.id}')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'blog/blog_details')