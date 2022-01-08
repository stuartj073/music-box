from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product

# Create your views here.


def product_review(request, product_id):
    """ Return the product review page. """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'reviews/product_review.html', context)
