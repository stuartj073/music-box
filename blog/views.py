from django.shortcuts import render, redirect, reverse, get_object_or_404
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


def delete_blog(request, blog_id):
    """ Delete specific blog post for user. """
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect(reverse('blog'))


def update_blog(request, blog_id):
    """ Allow user to update their own blog posts. """

    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method == "GET":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog_details', args=[blog.id]))
        else:
            print("Form invalid")
    else:
        form = BlogForm(instance=blog)

    context = {
        'blog': blog,
        'form': form,
    }

    return render(request, 'blog/update_blog.html', context)


def blog_details(request, blog_id):
    """ Show each blog on its individual page. """
    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_detail.html', context)
