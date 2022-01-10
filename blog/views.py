from django.shortcuts import render


# Create your views here.


def blog(request):
    """ Display all blog posts by users. """

    blog = Blog.object.all()

    context = {
        'blog': blog,
    }

    return render(request, "blog.html", context)