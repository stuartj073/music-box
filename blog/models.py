from django.db import models


# Create your models here.

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

    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    category = models.ForeignKey(Topic, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    """ 
    Allow users to comment on eachother's
    blog posts
    """
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    comment = models.TextField()

