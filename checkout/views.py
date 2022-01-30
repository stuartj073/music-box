from django.shortcuts import render, reverse
from .forms import OrderForm

# Create your views here.

def checkout(request):
    basket = request.session.get('basket', {})

    if not basket:
        messages.error(request, "Sorry, your bag is empty")
        return redirect(reverse('products'))
    
    if request.method == "POST":
        order_form = OrderForm(request.POST, request.FILES)
        if order_form.is_valid():
            order = form.save()
            messages.success(request, "Order saved")
            print("ORDER SAVED")
            return redirect(reverse('products'))
        else:
            print("Form invalid, please try again.")
            return redirect('checkout')
    else:
        # No data submitted
        order_form = OrderForm()()
    
    context = {
        'order_form': order_form,
    }

    return render(request, 'checkout.html', context)