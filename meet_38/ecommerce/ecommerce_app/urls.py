from django.urls import path, include
from ecommerce_app import views

urlpatterns = [
    path('', views.home, name = "Home"), 
    path('cart', views.cart, name = "Cart"),
    path('checkout', views.checkout, name = "Checkout"),
    path('categories', views.categories, name="Categories"),
    path('contacts', views.contacts, name="Contacts"),
    path('faqs', views.faqs, name="Faqs"),
    path('login', views.login, name="Login"),
    path('orders', views.orders, name="Orders"),
    path('register', views.register, name="Register"),
    path('shop', views.shop, name="Shop"),
]