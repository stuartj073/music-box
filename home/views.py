from django.shortcuts import render, reverse, redirect
from django.db.models import Q
from products.models import Product, Category

# Create your views here.

def index(request):
    """ Index page request. """
    """ Search bar request. """
    products = Product.objects.all()
    categories = Category.objects.all()

    if request.method == "GET":
        if 'search' in request.method:
            query = request.GET['search']
            if not query:
                print("You didn't specify your search")
                return redirect(reverse('home'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, 'home/index.html', context)



