from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecommerce_app/', include('ecommerce_app.urls')),
]
