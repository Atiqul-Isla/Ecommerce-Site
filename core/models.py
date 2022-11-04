from statistics import mode
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class ProductType(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField( max_length=255, unique=True, null=True, blank=True)
    image = models.ImageField(height_field=None, width_field=None, max_length=255, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name="sub_category", null=True, blank=True)
    title = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(height_field=None, width_field=None, max_length=255, null=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    price = models.FloatField()
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)   
    image = models.ImageField(height_field=None, width_field=None, max_length=255, null=True)
    stock = models.IntegerField()
    physical = models.BooleanField(default=True, null=True, blank=False)
    

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False) 
    trans_id = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity =  models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    region = models.CharField(max_length=255, null=False)
    country = models.CharField(max_length=255, null=False)
    zipcode = models.CharField(max_length=255, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0, null=True, 
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )
    title = models.CharField(max_length=255, null=True)
    comment = models.TextField(max_length=355)
    image = models.ImageField(height_field=None, width_field=None, max_length=255, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

