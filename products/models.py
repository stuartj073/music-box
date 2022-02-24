from django.db import models

# Create your models here.


class Category(models.Model):
    """
    Define the broad categories of goods sold on site.
    """
    class Meta:
        """ Adjust plural form in admin. """
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ Return string representation of name. """
        return self.name

    def get_friendly_name(self):
        """ Return string representation of type field. """
        return self.friendly_name


class Product(models.Model):
    """ More specific information about particular good. """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)                                 
    name = models.CharField(max_length=254)
    description = models.TextField()
    condition = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    warranty = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name
