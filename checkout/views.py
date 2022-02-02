from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import OrderForm
from django.contrib import messages
from django.conf import settings

from basket.contexts import basket_contents
from products.models import Product
from .models import OrderLineItem

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

    if request.method == "POST":
        basket = request.session.get('basket', {})

        form_data = {
            'first_name' : request.POST['first_name'],
            'second_name' : request.POST['second_name'],
            'email' : request.POST['email'],
            'phone_number' : request.POST['phone_number'],
            'street_address_1' : request.POST['street_address_1'],
            'street_address_2' : request.POST['street_address_2'],
            'town_or_city' : request.POST['town_or_city'],
            'county' : request.POST['county'],
            'postcode' : request.POST['postcode'],
        }
        order_form = OrderForm(data)
        if order_form.is_valid():
            order = order_form.save
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your basket wasn't "
                        "found in our database.")
                    )
                    order.delete()
                    return redirect(reverse('basket'))

            # Save user's info to profile
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, ('There was an error with your form.'))

    if not basket:
        messages.error(request, "Sorry, your basket is empty")
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

    print(intent)
    
    template = 'checkout/checkout.html'

    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """ 
    Render when checkout has been succesful
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successful! Your order number is {order_number}. \
                     An email will be sent to {order.email} shortly.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)