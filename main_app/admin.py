from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Banner)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ContactInfo)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Payment)



