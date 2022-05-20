from django.urls import path, include

from .views import products_list

urlpatterns = [
    path('', products_list),
]
