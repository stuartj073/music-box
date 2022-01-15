from django.shortcuts import render, reverse
from django.conf import settings

def basket_contents(request):
    """ Bag context processor for all apps. """
    
    basket = []
    total = 0
    basket_item_count = 0
    
    context = {
        'basket': basket,
        'total': total,
        'basket_item_count': basket_item_count,
    }

    return render(request, "basket.html", context)
