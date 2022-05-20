from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics


from .models import Product
from .serializers import ProductSerializer

# @api_view(['GET'])
# def products_list(request):
#     qs = Product.objects.all()
#     serialize = ProductSerializer(qs, many=True)
#     return Response(serialize.data)


class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailsAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
