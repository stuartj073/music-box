from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def basket(request):
    """ Show basket page for user. """

    context = {
        'basket': basket,
    }

    return render(request, "basket.html", context)


def add_to_basket(request, item_id):
    """ Add product to basket. """
    quantity = int(request.POST.get("amount"))
    redirect_url = request.POST.get("redirect_url")
    basket = request.session.get("basket", {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(request, "Item added")
    else:
        basket[item_id] = quantity
        messages.success(request, "Item added")

    request.session['basket'] = basket
    print(request.session['basket'])
    print("YEHO")

    return redirect(redirect_url)