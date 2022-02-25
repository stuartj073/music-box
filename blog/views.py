from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Topic, Blog, Comments
from .forms import BlogForm, CommentsForm
from django.contrib import messages
from profiles.models import Users

# Create your views here.


def blogs(request):
    """ Display all blog posts by users. """

    blogs = Blog.objects.all()
    topic = Topic.objects.all()

    context = {
        'blogs': blogs,
        'topic': topic,
    }

    return render(request, "blog/blogs.html", context)


@login_required
def add_blog(request):
    """ Add blog to blogs page. """
    user = get_object_or_404(Users, user=request.user)
    if request.method == "POST":
        form = BlogForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = request.user
            blog.save()
            messages.success(request, "Blog saved")
            return redirect(reverse('blog_details', args=[blog.slug]))
        else:
            print("Form invalid, please try again.")
            return redirect('blogs')
    else:
        # No data submitted
        form = BlogForm()

    template = 'blog/add_blog.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, slug):
    """ Delete specific blog post for user. """
    blog = Blog.objects.get(slug=slug)
    blog.delete()
    messages.success(request, "Blog deleted.")
    return redirect(reverse('blogs'))


@login_required
def update_blog(request, slug):
    """ Allow user to update their own blog posts. """

    blog = Blog.objects.get(slug=slug)

    if request.method == "POST":
        form = BlogForm(request.POST or None, request.FILES or None, instance=blog)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, "Blog has been updated.")
            return redirect(reverse('blog_details', args=[obj.slug]))
        else:
            messages.error("Form invalid, please try again.")
    else:
        form = BlogForm(instance=blog)

    context = {
        'blog': blog,
        'form': form,
    }

    return render(request, 'blog/update_blog.html', context)


def blog_details(request, slug):
    """ Show each blog on its individual page. """
    
    blog = Blog.objects.get(slug=slug)
    context = {}

    context['blog'] = blog

    if request.method == "POST":
        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            obj = comment_form.save(commit=False)
            obj.blog = blog
            obj.posted_by = request.user
            obj.save()
            messages.success(request, "Comment saved")
            return redirect('blog_details', slug=blog.slug)
        else:
            messages.error(request, "Something went wrong, please try again.")
            return redirect('blog')
    else:
        comment_form = CommentsForm()

    context = {
        'blog': blog,
        'comment_form': comment_form,
    }

    return render(request, 'blog/blog_detail.html', context)

