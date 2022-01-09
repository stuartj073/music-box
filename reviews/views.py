from django.shortcuts import render, get_object_or_404
from products.models import Product

# Create your views here.


def product_review(request, product_id):
    """ Show product review form. """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'reviews/product_reviews.html', context)


