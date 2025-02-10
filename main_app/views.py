from django.shortcuts import render,redirect

from .models import *

# Create your views here.


def index(request):
    banners = Banner.objects.all()
    product = Product.objects.all()
    
    context = {
        'banners': banners,
        'product': product,  # replace with your actual product model name and query.
    }
    return render(request, 'main_app/index.html',context)

def product_detail(request, id):
    product = Product.objects.get(id=id)  # replace with your actual product model name and query.
    related_products = Product.objects.filter(category=product.category).exclude(id=product.pk).order_by('?')[0:11]
    context = {
        'product': product,
        'related_products': related_products,  # replace with your actual product model name and query.  # replace with your actual product model name and query.  # replace with your actual product model name and query.  # replace with your actual product model name and query.  # replace with your actual product model name and query.  # replace with your actual product model name and query.  # replace with your actual product model name and query.  # replace with your actual
    }
    return render(request, 'main_app/product_detail.html',context)

from django.db.models import Q
def product_search(request):
    qurey = request.GET['q'] 
    lookup = Q(name__icontains = qurey) | Q(category__name__icontains = qurey) | Q(brand__name__icontains = qurey) 
    serach_product = Product.objects.filter(lookup)
    


    context ={
        'serach_product':serach_product
    }
    return render(request, 'main_app/product_search.html', context)


from main_app.forms import Contactfrom
def contact(request):
    if request.method == 'POST':
        form = Contactfrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return redirect('contact')
    return render(request, 'main_app/contact.html')