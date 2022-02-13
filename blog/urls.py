from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('add', views.add_blog, name='add_blog'),
    path('blog_details/<int:blog_id>', views.blog_details, name='blog_details'),
    path('delete/<int:blog_id>', views.delete_blog, name='delete_blog'),
    path('update/<int:blog_id>', views.update_blog, name='update_blog'),
    path('blog_comment/', views.blog_comment, name='blog_comment'),
]