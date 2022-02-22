from django.urls import path
from . import views

urlpatterns = [
    path('product_reviews/<int:product_id>', views.product_reviews, name='product_reviews'),
    path('add_review/<int:product_id>', views.add_review, name='add_review'),
    path('edit_review/<int:review_id>', views.edit_review, name='edit_review'),
    path('delete_review/<int:review_id>', views.delete_review, name='delete_review'),
    path('review_detail/<int:review_id>', views.review_detail, name='review_detail'),
]