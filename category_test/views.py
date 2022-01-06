from django.shortcuts import render, get_object_or_404
from products.models import Category, Product

# Create your views here.


def category(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'categories.html', context)


def category_details(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.all()

    context = {
        'category': category,
        'products': products,
    }

    return render(request, 'category_details.html', context)
