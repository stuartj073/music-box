from django.urls import path
from . import views

urlpatterns = [
    path('', views.category, name='category'),
    path('category_details/<int:category_id>', views.category_details, name='category_details'),
    path('records', views.records, name='records')
]
