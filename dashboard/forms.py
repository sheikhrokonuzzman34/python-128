from django import forms
from main_app.models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'regular_price', 'discount_price', 'descriptions', 'aditional_descriptions', 'stock', 'category', 'brand']
        widgets = {
            'descriptions': forms.Textarea(attrs={'rows': 3}),
            'aditional_descriptions': forms.Textarea(attrs={'rows': 3}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'img']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }        
