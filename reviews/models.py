from django.db import models
from products.models import Product, Category

# Create your models here.


class ProductReview(models.Model):
    """ Allow user to create review based on specific product."""
    name = models.ForeignKey(Product, null=True, blank=True,
                                 on_delete=models.SET_NULL)
    description = models.TextField()
    date = models.DateField(auto_now_add=True, blank=False,
                            null=False)

    def __str__(self):
        return self.name
