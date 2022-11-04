from webbrowser import get
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from . import forms 

# Create your views here.

# Creating a function based view to display all the products (Home)
def shop(request):
    products = models.Product.objects.all()
    product_types = models.ProductType.objects.all()
    context = {'products' : products, 'types' : product_types}
    return render(request, 'core/shop.html', context)

# Creating a function based view to display a cart 
def cart(request):
    context = {}
    return render(request, 'core/cart.html', context)

# Creating a view to display a checkouts
def checkout(request):
    context = {}
    return render(request, 'core/checkout.html', context)

def product(request, key):
    product = models.Product.objects.get(id=key)
    related_products = models.Product.objects.filter(category=product.category).exclude(id=key)[:4]
    if request.method == 'POST':
        rating = request.POST.get('rating', 3)
        title = request.POST.get('title', '')
        comment = request.POST.get('comment', '')

        review = models.Review.objects.create(product=product, user=request.user, rating=rating, title=title, comment=comment)
        return redirect(request.path_info)
    return render(request, 'core/product.html', {'product' : product, 'products' : related_products })

def category(request, slug):
    types = None
    categories = None
    products = models.Product.objects.all()
    if slug:
        types = models.ProductType.objects.get(slug=slug)
        categories = models.Category.objects.filter(product_type=types)
    context = {'categories' : categories,
               'products' : products,
               'types': types }
    return render(request, 'core/category.html', context)

def subCategory(request, slug):
    categories = None
    products = models.Product.objects.all()
    if slug:
        categories = models.Category.objects.get(slug=slug)
    context = {'categories' : categories,
               'products' : products}
    return render(request, 'core/sub-category.html', context)
    