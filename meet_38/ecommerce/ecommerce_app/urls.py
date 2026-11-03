from django.urls import path, include
from ecommerce_app import views

urlpatterns = [
    path('', views.home, name = "Home"), #esta era nuestra primer view
    path('contacts', views.contacts, name="Contacts"),
]