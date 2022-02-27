# from django.test import TestCase
# from .models import Blog, Comments, Topic


# class TestBlogModels(TestCase):
#     """
#     Test blog models
#     """
#     def setUp(self):
#         """
#         Create test blog
#         """
#         self.topic = Topic.objects.create(
#             name='Album',
#             friendly_name='Album1',
#         )
#         self.blog = Blog.objects.create(
#             title="Test",
#             topic=self.topic,
#             description="Testingalbum",
#         )

#     def test_blog_string(self):
#         self.assertEqual(str(self.blog), 'Test')
