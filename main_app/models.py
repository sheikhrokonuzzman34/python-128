from django.db import models

from django.utils import timezone

# Create your models here.

class ContactInfo(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    subject = models.CharField(max_length=450)
    message = models.TextField()
    
    class Meta:
        verbose_name = "Contact Information"
        
    def __str__(self):
        return self.email + ' ' + self.name
    

class Banner(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='banner_image/')
    product_name = models.CharField(max_length=400,null=True, blank=True)
    price = models.CharField(max_length=14)
    dis_price = models.CharField(max_length=14)
    class Meta:
        verbose_name_plural =("Banner")

    def __str__(self):
        return self.name
    
    
    
class Category(models.Model):
    name = models.CharField(max_length=50, null=False)
    img = models.ImageField(upload_to='category_images/', null=False,blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name  
    
    
class Brand(models.Model):
    name = models.CharField(max_length=50, null=False)
    img = models.ImageField(upload_to='category_images/', null=False,blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name
      
class Product(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='ProducImage')
    regular_price= models.PositiveIntegerField()
    discount_price= models.PositiveIntegerField(blank=True,null=True)
    descriptions =  models.TextField()
    aditional_descriptions =  models.TextField()
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural =("Products")

    def __str__(self):
        return self.name
    



from django.contrib.auth.models import User
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
    
    
class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s wishlist - {self.product.name}"    
    

    


    
        
    


