from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Topic, Blog, Comments
from .forms import BlogForm, CommentsForm
from django.contrib import messages
from profiles.models import Users

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


@login_required
def add_blog(request):
    """ Add blog to blogs page. """
    user = get_object_or_404(Users, user=request.user)
    if request.method == "POST":
        form = BlogForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.user = user
            blog.save()
            messages.success(request, "Blog saved")
            return redirect(reverse('blog_details', args=[blog.slug]))
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


@login_required
def delete_blog(request, slug):
    """ Delete specific blog post for user. """
    blog = Blog.objects.get(slug=slug)
    blog.delete()
    messages.success("Blog deleted.")
    return redirect(reverse('blog'))


@login_required
def update_blog(request, slug):
    """ Allow user to update their own blog posts. """

    blog = Blog.objects.get(slug=slug)

    if request.method == "POST":
        form = BlogForm(request.POST or None, request.FILES or None, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "Blog has been updated.")
            return redirect(reverse('blog_details', args=[blog.slug]))
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
    context = {}
    blog = Blog.objects.get(slug=slug)

    context['blog'] = blog

    if request.method == "POST":
        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save()
            comment.blog = blog
            comment.posted_by = request.user
            comment.save()
            messages.success(request, "Comment saved")
            return redirect(reverse('blog_details', slug=blog.slug))
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


# def blog_comment(request):
#     """ Allow user's to comment on blog posts """
#     blog = get_object_or_404(Blog, pk=blog_id)
#     if request.method == "POST":
#         comment_form = CommentsForm(request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save()
#             comment.blog = blog
#             comment.posted_by = request.user
#             comment.save()
#             messages.success(request, "Comment saved")
#             return redirect(reverse('blog_details', args=[blog.id]))
#         else:
#             messages.error(request, "Something went wrong, please try again.")
#             return redirect('blog')
#     else:
#         comment_form = CommentsForm()
    
#     template = 'blog/blog_details.html'

#     context = {
#         'comment_form': comment_form,
#     }

#     return redirect(request, template, context)