from django.shortcuts import render
from decimal import Decimal

# Create your views here.


def basket(request):
    """ Show basket page for user. """

    return render(request, "basket.html")
