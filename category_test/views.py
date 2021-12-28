from django.shortcuts import render, get_object_or_404
from products.models import Category

# Create your views here.


def category(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'categories.html', context)
