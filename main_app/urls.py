from django.urls import path

from main_app.views import *

urlpatterns = [
    path('', index, name='index'), 
    path('product_detail/<int:id>',product_detail, name='product_detail'),
    path('product_search',product_search, name='product_search'),
    path('contact/', contact, name='contact'), 

    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('increment/<int:item_id>/', increment_cart_item, name='increment_cart_item'),
    path('decrement/<int:item_id>/', decrement_cart_item, name='decrement_cart_item'),
    path('cart/', cart, name='cart'),
]