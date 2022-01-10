from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('add', views.add_blog, name='add_blog'),
]