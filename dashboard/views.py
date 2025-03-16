from django.shortcuts import render, redirect, get_object_or_404

from main_app.models import *
from dashboard.forms import *
from django.contrib import messages

# Create your views here.

from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from functools import wraps

from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect




def superuser_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Redirect to login page if the user is not authenticated
            return redirect('login_dashboard')
        elif request.user.is_superuser:
            # Allow access if the user is a superuser
            return view_func(request, *args, **kwargs)
        # Deny access for authenticated non-superusers
        return HttpResponseForbidden("You are not allowed to view this page.")
    return _wrapped_view


def login_dash(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  # Renamed for clarity
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')  # Fixed typo in redirect
        else:
            # Return an 'invalid login' error message.
            context = {'error_message': 'Username or Password is incorrect!'}
            return render(request, 'dashboard/signin.html', context)
    return render(request, 'dashboard/signin.html')




@superuser_required
def dashboard(request):
    return render(request, 'index.html')  # Render dashboard.html template



# Product crud operations
@superuser_required
def product_list(request):
    product = Product.objects.all()

    context = {
        'product': product
    }
    return render(request, 'product/product_list.html', context) 

@superuser_required
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

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_detail.html', {'product': product})

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


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, 'Product deleted successfully.')
    return redirect('product_list')


# Category crud operations
@superuser_required
def category_list(request):
    category = Category.objects.all()
    context = {
        'category': category
    }
    return render(request, 'category/category_list.html', context)
@superuser_required
def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully.')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category/category_add.html', {'form': form})

@superuser_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully.')
            return redirect('category_list')
        else:
            return redirect('category_add')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/category_add.html', {'form': form})

@superuser_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, 'Category deleted successfully.')
    return redirect('category_list')
