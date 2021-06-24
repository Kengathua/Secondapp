from rest_framework import serializers
from rest_framework.response import Response
from .models import Category, Product, Seller
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class CategorySerializer(ModelSerializer):
    random_photo = SerializerMethodField()

    def get_random_photo(selfself, obj):
        try:
            return obj.products.first().photo
        except:
            return ""

    class Meta:
        model = Category
        # fields =('name','author','price')
        fields = (
            'id',
            'name',
            'random_photo'
        )



class SellerSerializer(ModelSerializer):
    class Meta:
        model = Seller
        fields = (
            'id',
            'name',
        )


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'photo',
            'price',
            'title',
            'category',
            'seller',
            'photo'
        )


class ProductAllInfoSerializer(ModelSerializer):
    category = CategorySerializer()
    seller = SellerSerializer()

    class Meta:
        model = Product
        fields = (
            'id',
            'photo',
            'price',
            'title',
            'category',
            'seller',
            #'photo'
        )
