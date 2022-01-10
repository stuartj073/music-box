from django.shortcuts import render, get_object_or_404
from products.models import Product
from .models import ProductReview

# Create your views here.


def product_review(request, product_id):
    """ Show product review form. """

    product = get_object_or_404(Product, pk=product_id)

    product_reviews = ProductReview.objects.all()

    product_review = ProductReview()

    context = {
        'product': product,
        'product_reviews': product_reviews,
        'product_review': product_review,
    }

    return render(request, 'reviews/product_reviews.html', context)


