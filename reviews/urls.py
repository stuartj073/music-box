from django.urls import path
from . import views

urlpatterns = [
    path('product_reviews/', views.product_reviews, name='product_reviews'),
    path('add_review/<int:product_id>', views.add_review, name='add_review'),
    path('review_detail/<int:review_id>', views.review_detail, name='review_detail'),
]