from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('add', views.add_blog, name='add_blog'),
    path('blog_details/<int:blog_id>', views.blog_details, name='blog_details'),
]