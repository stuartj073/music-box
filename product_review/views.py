from django.shortcuts import render, get_object_or_404
from products.model import Product

# Create your views here.

def product_review(request, product_id):
    """ Return the product review page. """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return redirect(request, 'product_review.html', context)
