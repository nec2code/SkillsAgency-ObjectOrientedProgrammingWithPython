from django.shortcuts import render

# Create your views here.
def home(request):
      return render(request, "ecommerce_app/home.html")

def contacts(request):
      return render(request, "ecommerce_app/contacts.html")
