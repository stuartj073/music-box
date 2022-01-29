from django.shortcuts import render

# Create your views here.

def checkout(request):
    basket = request.session.get('basket', {})

    if not basket:
        messages.error(request, "Sorry, your bag is empty")
        return redirect(reverse('products'))

    order_form = OrderForm()
    
    context = {
        'order_form': order_form,
    }

    return render(request, 'checkout.html', context)