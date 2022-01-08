from django.urls import path
from . import views

urlpatterns = [
    path('product_review', views.product_review, name='product_review'),
]