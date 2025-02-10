from django.urls import path

from main_app.views import *

urlpatterns = [
    path('', index, name='index'), 
    path('product_detail/<int:id>',product_detail, name='product_detail'),
    path('product_search',product_search, name='product_search'),
    path('contact/', contact, name='contact'),  # Add your contact URL here.  # Add your contact URL here.  # Add your contact URL here.  # Add your contact URL here.  # Add your contact URL here.  # Add your contact URL here.  # Add your contact URL here.  # Add your contact URL here.  # Add your contact URL here.  # Add your contact URL here.  # Add your contact URL here.
]