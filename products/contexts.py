from django.shortcuts import render, reverse
from django.conf import settings
from django.shortcuts import get_object_or_404

from .models import Product, Category

def categories(request):
    """
    List of categories made available 
    for all apps
    """

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return context