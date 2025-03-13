from django.shortcuts import render, redirect, get_object_or_404

from main_app.models import Product
from dashboard.forms import ProductForm
from django.contrib import messages

# Create your views here.

def dashboard(request):
    return render(request, 'index.html')  # Render dashboard.html template


def product_list(request):
    product = Product.objects.all()

    context = {
        'product': product
    }
    return render(request, 'product/product_list.html', context) 

def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully.')
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product/product_add.html',{'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('product_list')
        else:
            return redirect('product_add')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/product_add.html', {'form': form})



