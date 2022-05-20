from django.urls import path, include

from .views import (
    ProductListAPIView,
    ProductDetailsAPIView
)

urlpatterns = [
    path('', ProductListAPIView.as_view()),
    path('<int:pk>', ProductDetailsAPIView.as_view()),
]
