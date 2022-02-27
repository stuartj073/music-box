from django.test import TestCase
from .forms import BlogForm, CommentsForm


class TestBlogForm(TestCase):
    """
    Tests for blog form 
    """

    def test_title_is_required(self):
        form = BlogForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_description_is_required(self):
        form = BlogForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0], 'This field is required.')

    def test_image_field_is_not_required(self):
        form = BlogForm({'title': 'Test'})
        self.assertTrue(form.is_valid)


class TestCommentForm(TestCase):
    """
    Tests for comment form
    """
    def test_comment_is_required(self):
        form = CommentsForm({'comment': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('comment', form.errors.keys())
        self.assertEqual(form.errors['comment'][0], 'This field is required.')