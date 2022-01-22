from django.shortcuts import render, get_object_or_404, redirect, reverse
from products.models import Product
from django.contrib import messages
from .forms import ProductReviewForm

# Create your views here.


def product_review(request, product_id):
    """ Show product review form. """

    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == "POST":
        form = ProductReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            messages.success(request, "Review saved")
            print("YAP")
            return redirect(reverse('product_review', args=[review.id]))
        else:
            print("Form is invalid")
            return redirect(reverse("product_review"))

    else:
        form = ProductReviewForm()
        form.save()



