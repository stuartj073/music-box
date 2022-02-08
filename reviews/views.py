from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import Product
from .models import ProductReview
from django.contrib import messages
from .forms import ProductReviewForm

# Create your views here.


def product_reviews(request, product_id):
    """ Show product review form. """

    reviews = ProductReview.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'product_reviews.html', context)


def add_review(request, product_id):
    """ 
    Render form to allow user to write review on 
    any given product
    """
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form = ProductReviewForm(request.FILES, reuqest.POST, instance=product)
        if form.is_valid():
            messages.success(request, "New product review created.")
            form.save()
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




