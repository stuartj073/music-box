from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Product, Category
from django.db.models import Q
from django.contrib import messages
from .forms import ProductForm

# Create your views here.


def products(request):
    """ Show all products along with search and sort features. """

    products = Product.objects.order_by('-price')
    query = None
  
    if request.method == "GET":

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, ("You didn't specify your search"))
                return redirect(reverse('products'))
       
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            if not products:
                print("Sorry nothing was found")
        
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

                
    context = {
        'products': products,
        'search_term': query,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)


def records(request):
    """ Returns all vinyl records from products. """

    products = Product.objects.all()

    context = {
        'product': products,
    }

    return render(request, "products/records.html", context)


def add_product(request):
    """ Present add product form to user based off the model. """

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            product = form.save()
            return redirect('products')
        else:
            print("Form invalid")
            return reverse("products")
    else:
        #  No data submitted
        form = ProductForm()

    template = 'products/add_product.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    """ Delete specific blog post for user. """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect(reverse('products'))





