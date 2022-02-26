from django.db import models
from products.models import Product, Category
from django.contrib.auth.models import User


class ProductReview(models.Model):
    """
    Allow user to create review based on a specific product
    """
    name = models.ForeignKey(Product, null=True, blank=True,
                             on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    title = models.TextField(max_length=30, default="Review Title")
    description = models.TextField()
    date = models.DateField(auto_now_add=True, blank=False,
                            null=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
