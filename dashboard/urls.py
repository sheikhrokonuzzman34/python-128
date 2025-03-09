from django.urls import path

from dashboard.views import *

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'), 
    
    
    
]