from django.shortcuts import render
from .models import Blog

# Create your views here.


def blog(request):
    """ Display all blog posts by users. """

    blog = Blog.objects.all()

    context = {
        'blog': blog,
    }

    return render(request, "blog/blog.html", context)
