from django.urls import path

from dashboard.views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'), 
    path('login_dash/',login_dash,name='login_dashboard'),

    path('product_list/', product_list, name='product_list'),
    path('product_add/', product_add, name='product_add'),
    path('products/edit/<int:pk>/', product_edit, name='product_edit'),
    path('products/delete/<int:pk>/', product_delete, name='product_delete'),
    path('pproduct_detail_dashboard/<int:pk>/', product_detail, name='product_detail_dashboard'),




    path('category_list/', category_list, name='category_list'),
    path('category_add/', category_add, name='category_add'),
    path('category/edit/<int:pk>/', category_edit, name='category_edit'),
    path('category/delete/<int:pk>/', category_delete, name='category_delete'),
    
    
    
]