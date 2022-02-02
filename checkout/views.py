from django.shortcuts import render, reverse, redirect
from .forms import OrderForm
from django.contrib import messages
from django.conf import settings

from basket.contexts import basket_contents

import stripe

# Create your views here.

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})
    current_basket = basket_contents(request)
    total = current_basket['checkout_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    if not basket:
        messages.error(request, "Sorry, your bag is empty")
        return redirect(reverse('products'))

    if not stripe_public_key:
        messages.error(request, "Stripe public key is missing. \
                    Please check environment configurations.")
    
    if request.method == "POST":
        order_form = OrderForm(request.POST, request.FILES)
        if order_form.is_valid():
            order = order_form.save()
            messages.success(request, "Order saved")
            print("ORDER SAVED")
            return redirect(reverse('products'))
        else:
            print("Form invalid, please try again.")
            return redirect('checkout')
    else:
        # No data submitted
        order_form = OrderForm()
    
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)