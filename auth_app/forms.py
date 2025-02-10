from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from auth_app.models import *


class RegisterForm(UserCreationForm):
       class Meta:
        model = User 
        fields = ['first_name','last_name','username','email','password1','password2']