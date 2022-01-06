from django.shortcuts import render, reverse, redirect
from django.db.models import Q
from products.models import Product, Category
from django.contrib import messages

# Create your views here.

def index(request):
    """ Index page request. """
    """ Search bar request. """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)

