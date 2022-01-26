from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

# Create your views here.


def basket(request):
    """ Show basket page for user. """

    context = {
        'basket': basket,
    }

    return render(request, "basket.html", context)


def add_to_basket(request, item_id):
    """ View to add product and/or sizes to basket. """

    product = get_object_or_404(Product, pk=item_id)
    amount = int(request.POST.get('amount'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {basket
    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][siamount
                messages.success(request,
                                 (f'Updated size {size.upper()} '
                                  f'{product.name} amount to '
                                  f'{basket[item_id]["items_by_size"][size]}'))
            else:
                basket[item_id]['items_by_size'][size] = amount
                messages.success(request,
                                 (f'Added size {size.upper()} '
                                  f'{product.name} to your basket'))
        else:
            basket[item_id] = {'items_by_size': {size: amount}}
            messages.success(request,
                             (f'Added size {size.upper()} '
                              f'{product.name} to your basket'))
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += amount
            messages.success(request,
                             (f'Added {product.name} '
                              f'amount to {basket[item_id]}'))
        else:
            basket[item_id] = amount
            messages.success(request, f'{product.name} has been added to your basket.')

    request.session['basket'] = basket
    return redirect(redirect_url)


def edit_basket(request, item_id):
    """Edit the amount of any given product in the basket."""

    product = get_object_or_404(Product, pk=item_id)
    amount = int(request.POST.get('amount'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    basket = request.session.get('basket', {})

    if size:
        if amount > 0:
            basket[item_id]['items_by_size'][size] = amount
            messages.success(request,
                             (f'Updated size {size.upper()} '
                              f'{product.name} amount to '
                              f'{basket[item_id]["items_by_size"][size]}'))
        else:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
            messages.success(request,
                             (f'Adjusted size {size.upper()} '
                              f'{product.name} from your basket'))
    else:
        if amount > 0
            basket[item_id] = amount
            messages.success(request,
                             (f'Updated {product.name} '
                              f'amount to {basket[item_id]}'))
        else:
            basket.pop(item_id)
            messages.success(request,
                             (f'Removed {product.name} '
                              f'from your basket'))

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))
