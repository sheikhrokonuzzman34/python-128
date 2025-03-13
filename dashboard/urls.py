from django.urls import path

from dashboard.views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'), 

    path('product_list/', product_list, name='product_list'),
    path('product_add/', product_add, name='product_add'),
    path('products/edit/<int:pk>/', product_edit, name='product_edit'),
    
    
    
]