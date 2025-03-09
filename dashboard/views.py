from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'index.html')  # Render dashboard.html template


def product_list(request):
    return render(request, 'product_list.html')  



