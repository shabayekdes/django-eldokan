from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Product
from .serializers import ProductSerializer

@api_view(['GET'])
def products_list(request):
    qs = Product.objects.all()
    serialize = ProductSerializer(qs, many=True)
    return Response(serialize.data)
