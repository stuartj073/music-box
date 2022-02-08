from django.urls import path
from . import views

urlpatterns = [
    path('product_reviews/<int:product_id>', views.product_review, name='product_review'),
    path('add_review/<int:product_id>', views.add_review, name='add_review'),
]