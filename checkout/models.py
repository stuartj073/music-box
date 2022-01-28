import uuid

from django.db import models
from django_countries.fields import CountryField
from django.db.models import Sum
from django.conf import settings
from product.models import Product

# Create your models here.

class Order(models.Model):
    """ Information needed for each transaction. """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    surname = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=50, null=True, blank=True)
    country = CountryField(null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)


class OrderLineItem(models.Model):
    """ Information on individual item in a basket. """
    order = models.ForeignKey(Order, null=False, blank=False,on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)