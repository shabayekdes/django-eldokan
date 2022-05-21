from django.urls import path, include

from .views import (
    ProductListAPIView,
    ProductDetailsAPIView,
    product_create,
    product_detail
)

urlpatterns = [
    path('', ProductListAPIView.as_view()),
    path('<int:pk>', ProductDetailsAPIView.as_view()),
    path("create/", product_create, name="product_create"),
    path("<int:id>/detail", product_detail, name="products-detail")
]
