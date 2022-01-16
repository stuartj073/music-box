from django.shortcuts import render

# Create your views here.


def basket(request):
    """ Show basket page for user. """

    return render(request, "basket.html")
