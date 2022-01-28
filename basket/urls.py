from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket, name='basket'),
    path('add_to_basket/<item_id>', views.add_to_basket, name='add_to_basket'),
    path('remove/<item_id>', views.remove_from_basket, name='remove_from_basket'),
    path('edit/<item_id>', views.edit_basket, name='edit_basket'),
]
