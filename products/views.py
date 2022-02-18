from django.shortcuts import render, redirect, get_object_or_404, reverse

from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import ProductForm
from .models import Product, Category

# Create your views here.


def products(request):
    """ Show all products along with search and sort features. """

    products = Product.objects.order_by('-price')
    query = None
    categories = None
    sort = None
    direction = None

    if request.method == "GET":
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

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
            
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    categories = Category.objects.all()

    context = {
        'products': products,
        'search_term': query,
        'categories': categories,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)


def product_cat(request, category_id):
    """
    Return all products associated with category
    """
    category = get_object_or_404(Category, pk=category_id)
    products = Product.objects.filter(category=category)

    template = 'products/product.html'

    context = {
        'category': category,
        'products': products,
    }

    return render(request, template, context)


@login_required
def add_product(request):
    """ Present add product form to user based off the model. """
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            product = form.save()
            messages.success(request, "Product added.")
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


@login_required
def edit_product(request, product_id):
    """ Allow user to update their own blog posts. """

    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"Successfully updated {product.name}.")
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            print("Form invalid")
            messages.error(request, f"Failed to update product description.")
    else:
        form = ProductForm(instance=product)

    template = 'products/edit_product.html'
    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete specific blog post for user. """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted")
    return redirect(reverse('products'))
