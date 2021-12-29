from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('product_details/', views.product_detail, name='product_detail'),
]