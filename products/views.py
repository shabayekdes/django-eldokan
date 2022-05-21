from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics


from .models import Product
from .forms import ProductForm
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


def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        obj = form.save()
        return redirect(obj.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'products/create.html', context=context)

def product_detail(request, id):
    obj = Product.objects.get(id=id)
    context = {
        'object': obj
    }
    return render(request, 'products/details.html', context=context)
