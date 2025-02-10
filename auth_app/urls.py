from django.urls import path

from auth_app.views import *

urlpatterns = [
    path('register/', register, name='register'), 
    path('login_page/', login_page, name='login_page'), 
    path('logout_view/', logout_view, name='logout_view'), 
    
    
    
]