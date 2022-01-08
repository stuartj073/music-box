from django.urls import path
from . import views

urlpatterns = [
    path('product_review/<int:product_id>', views.product_review, name='product_review'),
]