from django.urls import path

from auth_app.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'), 
    path('login_page/', login_page, name='login_page'), 
    path('logout_view/', logout_view, name='logout_view'), 

    path('profile/update',profileupdate,name='profileupdate-page'),
    path('profile/',profile,name='profile-page'),

    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='passwordchanage.html'),name='password-change'),
    path('password_change/done',auth_views.PasswordChangeDoneView.as_view(template_name='passwordchanage_done.html'),name='password_change_done'),
    

    path('reset-password/', password_reset, name='reset_password'),
    path('reset-password-done/', password_reset_done, name='reset_password_done'),
    path('reset-password-confirm/<uidb64>/<token>/', password_reset_confirm, name='reset_password_confirm'),
    path('reset-password-complete/', password_reset_complete, name='password_reset_complete'),
    
    
]