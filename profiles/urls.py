from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('orders/<order_number>', views.orders, name='orders'),
]