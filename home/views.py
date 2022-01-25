from django.shortcuts import render
from django.db.models import Q
from products.models import Product, Category
from django.contrib import messages

# Create your views here.


def index(request):
    """ Index page request. """
    products = print("hello")
   
    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)
