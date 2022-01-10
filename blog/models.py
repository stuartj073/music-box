from django.db import models

# Create your models here.


class Blog(models.Model):
    """ Allow users to create blog posts on all things music. """

    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        """ Return the blog post's name as it's title. """
        return self.name()
