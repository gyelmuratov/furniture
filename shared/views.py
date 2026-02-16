from urllib import request

from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request, 'home.html')

def contact_view(request):
    return render(request, 'contact.html')

def account_view(request):
    return render(request, 'account.html')

def login_view(request):
    return render(request, 'login.html')

def blog_view(request):
    return render(request, 'blog-detail.html')

def blog_list_view(request):
    return render(request, 'blog-list.html')

def checkout_view(request):
    return render(request, 'checkout.html')

def product_view(request):
    return render(request, 'product-detail.html')

def products_list_view(request):
    return render(request, 'products-list.html')

def register_view(request):
    return render(request, 'register.html')

def reset_password_view(request):
    return render(request, 'reset-password.html')

def about_us_view(request):
    return render(request, 'about-us.html')

def data_not_found_view(request):
    return render(request, '404.html')

def cart_view(request):
    return render(request, 'cart.html')