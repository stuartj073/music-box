from django.shortcuts import render, get_object_or_404
from .models import Users
from django.contrib import messages

from .models import Users
from .forms import UserForm

from checkout.models import Order

# Create your views here.

def profile(request):
    """ Display a user's profile. """
    profile = get_object_or_404(Users, user=request.user)

    if request.method == "POST":
        form = UserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Shipping info updated")
        else:
            messages.error(request, "Info not saved. Try again.")
    else:
        form = UserForm()

    context = {
        'form': form,
        'on_profile': True,
    }

    template = 'profiles/profiles.html'

    return render(request, template, context)


def orders(request, order_number):
    """
    Show each order associated with logged in user
    """
    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    
    context = {
        'order': order,
        'from_profile': from_profile,
    }

    return render(request, template, context)