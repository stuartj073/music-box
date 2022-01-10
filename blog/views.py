from django.shortcuts import render, redirect, reverse
from .models import Topic, Blog
from .forms import BlogForm

# Create your views here.


def blog(request):
    """ Display all blog posts by users. """

    blogs = Blog.objects.all()
    topic = Topic.objects.all()

    context = {
        'blogs': blogs,
        'topic': topic,
    }

    return render(request, "blog/blog.html", context)


def add_blog(request):
    """ Add blog to blogs page. """
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            print("Blog saved")
            return redirect('blog')
        else:
            print("Form invalid, please try again.")
            return redirect('blog')
    else:
        # No data submitted
        form = BlogForm()

    template = 'blog/add_blog.html'

    context = {
        'form': form,
    }

    return render(request, template, context)
