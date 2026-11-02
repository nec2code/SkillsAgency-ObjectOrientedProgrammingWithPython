from django.urls import path
from ecommerce_stage_01.views import *

urlpatterns = [
    path('', home, name="Home"),
    path('cart', cart, name="Cart"),
    path('categories/', categories),
    path('checkout/', checkout),
    path('contacts/', contacts),
    path('error404/', error404),
    path('faqs/', faqs),
    path('home/', home),
    path('itemdetail/', itemdetail),
    path('login/', login),
    path('orderdetail/', orderdetail),
    path('orders/', orders),
    path('shop/', shop),
    path('signup/', signup),
    path('whishlist/', whishlist)
]   
