from django.shortcuts import render, reverse, redirect
from .forms import OrderForm
from django.contrib import messages

# Create your views here.

def checkout(request):
    basket = request.session.get('basket', {})

    if not basket:
        messages.error(request, "Sorry, your bag is empty")
        return redirect(reverse('products'))
    
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
        'stripe_public_key': 'pk_test_51KOR5pF4c4G15bFhDBWJcD3dHL21GSDy29nh14KLTkwkCEHToCNnXopNKekdu2EQbencBwlYG3KoTnqSMyxyMOFk00StSAVqYS'
        'client_secret': 'test client secret',
    }

    return render(request, template, context)