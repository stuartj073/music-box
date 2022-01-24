from django.shortcuts import render, reverse
from django.conf import settings
from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product

def basket_contents(request):
    """ Basket context processor for all apps. """
    
    basket_items = []
    total = 0
    basket_item_count = 0
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        basket_item_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })


    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE /100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    checkout_total = delivery + total
    
    context = {
        'basket_items': basket_items,
        'total': total,
        'basket_item_count': basket_item_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'checkout_total': checkout_total,
        'basket': basket,
    }

    return context
