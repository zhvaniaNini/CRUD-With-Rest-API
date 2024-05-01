from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from store.models import Product

class ProductListSerializer(ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['name', 'price']


class ProductDetailSerializer(ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'category']

class CreateProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class UpdateProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['stock']

class DeleteProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        