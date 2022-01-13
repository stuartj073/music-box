from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('product_details/<int:product_id>', views.product_detail, name='product_detail'),
    path('records/', views.records, name='records'),
    path('add_product/', views.add_product, name='add_product'),
]
