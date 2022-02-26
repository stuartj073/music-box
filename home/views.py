from django.shortcuts import render
from django.db.models import Q
from products.models import Product, Category
from django.contrib import messages


def index(request):
    """
    Index page request
    """

    return render(request, 'home/index.html')


def error_404(request, exception):
    """
    A view to return the 404 page
    """

    return render(request, '404.html')


def error_500(request, exception=None):
    """
    A view to return the 500 page
    """

    return render(request, '500.html')


def error_403(request, exception=None):
    """
    A view to return the 403 page
    """

    return render(request, '403.html')