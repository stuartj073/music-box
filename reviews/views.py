from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from products.models import Product
from .models import ProductReview
from .forms import ProductReviewForm

from profiles.models import Users


def product_reviews(request, product_id):
    """ Show product review form. """
    product = get_object_or_404(Product, pk=product_id)

    reviews = ProductReview.objects.filter(name=product)

    template =  'reviews/product_reviews.html'

    context = {
        'reviews': reviews,
    }

    return render(request, template, context)


def review_detail(request, review_id):
    """ 
    Show individual review
    """
    review = get_object_or_404(ProductReview, pk=review_id)

    template = 'reviews/review_details.html'

    context = {
        'review': review,
    }

    return render(request, template, context)


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
            return redirect(reverse('review_detail', args=[review.id]))
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


def edit_review(request, review_id):
    """
    Allow a user to edit their review
    """
    review = get_object_or_404(ProductReview, pk=review_id)

    if request.method == "POST":
        form = ProductReview(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, f"Successfully updated review.")
            return redirect(reverse('review_details', args=[review.id]))
        else:
            print("Form invalid")
            messages.error(request, f"Failed to update review.")
    else:
        form = ProductReview()

    template = 'reviews/edit_review.html'

    context = {
        'review': review,
        'form': form,
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

