from django.shortcuts import render, redirect, get_objects_or_404
from .models import Product, Category

# Create your views here.


def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'products/products.html', context)
