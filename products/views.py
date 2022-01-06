from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Product
from django.db.models import Q
from django.contrib import messages

# Create your views here.


def products(request):
    """ Show all products along with search and sort features. """

    products = Product.objects.all()
    query = None
  
    if request.method == "GET":
        if 'q' in request.GET:
            print("Hello there")
            query = request.GET['q']
            if not query:
                messages.error(request, ("You didn't specify your search"))
                return redirect(reverse('products'))
       
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)


def records(request):
    """ Returns all vinyl records from products. """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, "products/records.html", context)
