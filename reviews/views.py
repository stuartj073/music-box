from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from products.models import Product
from .models import ProductReview
from .forms import ProductReviewForm

from profiles.models import Users


def product_reviews(request, product_id):
    """ Show product review form. """
    product = get_object_or_404(Product, pk=product_id)
    reviews = ProductReview.objects.get(name=product_id)

    context = {
        'reviews': reviews,
    }

    return render(request, 'product_reviews.html', context)


def add_review(request, product_id):
    """ 
    Render form to allow user to write review on 
    any given product
    """
    user = Users.objects.get(user=request.user)
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        form = ProductReviewForm(request.POST)
        print(form.errors)
        if form.is_valid():
            review = form.save()
            review.name = product
            review.user = user 
            review.save()
            messages.success(request, "New product review created.")
        else:
            messages.error(request, "Form invalid, please try again.")
            return redirect(reverse('product_details', args=[product.id]))
    else:
        form = ProductReviewForm()

    template = 'reviews/add_review.html'

    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def review_details(request, productreview_id):
    """
    Show the individual review page of each item
    """
    review = get_object_or_404(ProductReview, pk=productreview_id)

    context = {
        'review': review,
    }

    return render(request, 'products/product_details.html', context)

