from django.shortcuts import render

# Create your views here.
def home(request):
      return render(request, "ecommerce_app/home.html")

def cart(request):
      return render(request, "ecommerce_app/cart.html")

def checkout(request):
      return render(request, "ecommerce_app/checkout.html")

def categories(request):
      return render(request, "ecommerce_app/categories.html")

def contacts(request):
      return render(request, "ecommerce_app/contacts.html")

def faqs(request):
      return render(request, "ecommerce_app/faqs.html")

def login(request):
      return render(request, "ecommerce_app/login.html")

def orders(request):
      return render(request, "ecommerce_app/orders.html")

def register(request):
      return render(request, "ecommerce_app/register.html")

def shop(request):
      return render(request, "ecommerce_app/shop.html")
