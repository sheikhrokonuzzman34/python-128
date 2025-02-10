
from django import forms
from .models import *


class Contactfrom(forms.ModelForm):
     class Meta:
        model = ContactInfo
        fields = '__all__'