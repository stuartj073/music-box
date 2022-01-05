from django.db import models
from products.models import Category
from django.contrib.auth.models import User

# Create your models here.

class Users(models.Model):
    """ Model to display the info needed to register account. """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    area_of_interest = models.ForeignKey(Category, on_delete)
    default_phone_number = models.CharField(max_length=20,
                                            null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40,
                                            null=True, blank=True)
    default_county = models.CharField(max_length=80,
                                      null=True, blank=True)
    default_postcode = models.CharField(max_length=20,
                                        null=True, blank=True)
    default_country = CountryField(blank_label='Country',
                                   null=True, blank=True)


