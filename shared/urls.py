from django.urls import path
from shared.views import (
    home_page_view,
    contact_view,
    account_view,
    login_view,
    blog_view,
    blog_list_view,
    checkout_view,
    product_view,
    products_list_view,
    register_view,
    reset_password_view,
    about_us_view,
    data_not_found_view,
    cart_view,
)

app_name = 'shared'

urlpatterns = [

    path('', home_page_view, name='home'),

    path('contact/', contact_view, name='contact'),

    path('account/', account_view, name='account'),

    path('login/', login_view, name='login'),

    path('blog/', blog_view, name='blog-detail'),

    path('blogs/', blog_list_view, name='blog-list'),

    path('checkout/', checkout_view, name='checkout'),

    path('product/', product_view, name='product-detail'),

    path('products/', products_list_view, name='products-list'),

    path('register/', register_view, name='register'),

    path('reset-password/', reset_password_view, name='reset-password'),

    path('cart/',cart_view, name='cart'),

    path('about-us/', about_us_view, name='about-us'),

    path('404/', data_not_found_view, name='404.html'),

]
