from django.shortcuts import render, reverse
from django.conf import settings
from decimal import Decimal

def basket_contents(request):
    """ Bag context processor for all apps. """
    
    basket = []
    total = 0
    basket_item_count = 0

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE /100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    checkout_total = delivery + total
    
    context = {
        'basket': basket,
        'total': total,
        'basket_item_count': basket_item_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'checkout_total': checkout_total,
    }

    return context
