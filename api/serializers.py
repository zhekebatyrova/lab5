from rest_framework import serializers
from .models import Product, Category


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    price = serializers.FloatField()
    description = serializers.CharField()
    quantity = serializers.IntegerField()
    is_active = serializers.BooleanField()


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'quantity', 'is_active')


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
