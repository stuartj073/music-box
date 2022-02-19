from django.db import models
from profiles.models import Users

from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Topic(models.Model):
    """ Allow user to select a topic to blog about. """
    class Meta:
        """ Adjust plural form in admin. """
        verbose_name_plural = "Topics"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ Return string representation of name. """
        return self.name

    def get_friendly_name(self):
        """ Return string representation of type field. """
        return self.friendly_name


class Blog(models.Model):
    """ Allow users to create blog posts on all things music. """

    title = models.CharField(max_length=50)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default="")
    image = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name



def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(f'{instance.user} - {instance.title}')


pre_save.connect(pre_save_blog_post_receiver, sender=Blog)


class Comments(models.Model):
    """ 
    Allow users to comment on eachother's
    blog posts
    """
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    comment = models.TextField()

