from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required


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



@login_required(login_url='login_page')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required(login_url='login_page')
def increment_cart_item(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

@login_required(login_url='login_page')
def decrement_cart_item(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()  # Remove item if quantity is 1 and decrement is pressed
    return redirect('cart')

@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.product.regular_price * item.quantity for item in cart_items)
    return render(request, 'main_app/cart.html', {'cart_items': cart_items, 'total': total})


@login_required(login_url='login_page')
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('wishlist')


@login_required(login_url='login_page')
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'main_app/wishlist.html', {'wishlist_items': wishlist_items})



@login_required
def checkout(request):
    if request.method == 'POST':
        cart_items = Cart.objects.filter(user=request.user)
        total_price = sum(item.product.regular_price * item.quantity for item in cart_items)

        # Handle shipping address
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        delivery_area = request.POST.get('delivery_area')

        # Add delivery charge
        if delivery_area == 'inside_dhaka':
            delivery_charge = 100
        else:
            delivery_charge = 150

        # Add the delivery charge to the total price
        total_price += delivery_charge

        # Create order and order items
        order = Order.objects.create(user=request.user, total_price=total_price)
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.regular_price
            )

        # Clear the cart
        cart_items.delete()

        return redirect('/', order_id=order.id)

    # Calculate total price for GET requests
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.regular_price * item.quantity for item in cart_items)

    # Prepare context for the template
    delivery_area_charge = {
        'inside_dhaka': 100,
        'outside_dhaka': 150
    }

    context = {
        'total_price': total_price,
        'delivery_area_charge': delivery_area_charge,
    }

    return render(request, 'main_app/checkout.html', context)