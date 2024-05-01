from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from store.models import Product
from store.serializers import ProductDetailSerializer, ProductListSerializer, CreateProductSerializer, UpdateProductSerializer, DeleteProductSerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

# Create your views here.


class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_url_kwarg = 'product_id'

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class CreateProduct(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer

class UpdateProduct(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = UpdateProductSerializer
    lookup_url_kwarg = 'product_id'

class DeleteProduct(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = DeleteProductSerializer
    lookup_url_kwarg = 'product_id'