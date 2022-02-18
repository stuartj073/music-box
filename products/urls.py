from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('product_details/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('product_cat/<int:category_id>/', views.product_cat, name='product_cat'),
]
