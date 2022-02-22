from django.urls import path
from . import views

urlpatterns = [
    path('blogs', views.blogs, name='blogs'),
    path('add', views.add_blog, name='add_blog'),
    path('<slug:slug>/', views.blog_details, name='blog_details'),
    path('delete/<slug:slug>/', views.delete_blog, name='delete_blog'),
    path('update/<slug:slug>/', views.update_blog, name='update_blog'),
    # path('blog_comment/', views.blog_comment, name='blog_comment'),
]