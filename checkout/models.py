import uuid

from django.db import models
from django_countries.fields import CountryField
from django.db.models import Sum
from decimal import Decimal
from django.conf import settings

from products.models import Product
from profiles.models import Users

class Order(models.Model):
    """ 
    Information needed for each transaction
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True,
                                     blank=True, related_name='orders')
    first_name = models.CharField(max_length=30, null=False, blank=False)
    surname = models.CharField(max_length=30, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=50, null=True, blank=True)
    country = CountryField(blank_label='Please select country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    checkout_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    class Meta:
        ordering = ['-date']

    def _generate_order_number(self):
        """ 
        Create unique order number
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update checkout total for every line item added.
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        
        self.checkout_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """ 
        Overide save method ensuring an order number is
        created incase it wasn't.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number



class OrderLineItem(models.Model):
    """ 
    Information on individual item in a basket 
    """
    order = models.ForeignKey(Order, null=False, blank=False,on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'