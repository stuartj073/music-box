from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.views.decorators.http import require_POST

from .forms import OrderForm
from .models import Order, OrderLineItem
from basket.contexts import basket_contents
from products.models import Product

from profiles.models import Users
from profiles.forms import UserForm


import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.success(request, ('Sorry, your payment cannot be '
                                 'processed right now. Please try '
                                 'again later.'))
        print("form failed")
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        basket = request.session.get('basket', {})

        form_data = {
            'first_name' : request.POST['first_name'],
            'surname' : request.POST['surname'],
            'email' : request.POST['email'],
            'phone_number' : request.POST['phone_number'],
            'street_address1' : request.POST['street_address1'],
            'street_address2' : request.POST['street_address2'],
            'town_or_city' : request.POST['town_or_city'],
            'county' : request.POST['county'],
            'postcode' : request.POST['postcode'],
        }
        order_form = OrderForm(form_data)
        print("UPPAA", intent)
        
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_basket = json.dumps(bag)
            order.save()
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
                    messages.success(request, (
                        "One of the products in your basket wasn't "
                        "found in our database.")
                    )
                    order.delete()
                    return redirect(reverse('basket'))
                print("YES LAD", intent)

            # Save user's info to profile
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.success(request, ('There was an error with your form.'))
            print("OH YA", intent)
    else:
        print("OH NO", intent)
        basket = request.session.get('basket', {})
        if not basket:
            messages.success(request, "Sorry, your basket is empty")
            return redirect(reverse('products'))

        current_basket = basket_contents(request)
        total = current_basket['checkout_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()
    
    if not stripe_public_key:
        messages.success(request, 'Stripe public key is missing. \
            Check your environment variables.')

    template = 'checkout/checkout.html'

    print("intent is defined as", intent)
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