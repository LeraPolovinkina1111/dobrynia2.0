from django.contrib import admin
from django.urls import path
from carts import views

from django.urls import path

app_name = 'carts'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('home/', views.home, name='home'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
