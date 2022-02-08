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

    context ={
        'product': product,
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
            return render(reverse("add_product", args=[product.id]))
    else:
        form = ProductReviewForm()

    template = 'reviews/add_review.html'

    context = {
        'form': form,
    }

    return render(request, template, context)




