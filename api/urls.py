from django.urls import path, include

from .views import api_home

urlpatterns = [
    path('', api_home),
    path('products/' , include('products.urls')),
]
