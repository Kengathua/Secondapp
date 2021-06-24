from django.db.models.deletion import CASCADE
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from django.http import Http404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.utils import timezone
from rest_framework.viewsets import ModelViewSet
from .models import Seller, Category, Product

from .serializers import SellerSerializer, ProductSerializer, CategorySerializer


class ProductList:
    @api_view(['GET'])
    def apiOverview(request):
        api_urls = {
            'List': '/product-list/',
            'Details View': '/product-detail/<int:id>',
            'Create': '/product-create/',
            'Update': 'product-update/<int:id>',
            'Delete': '/product-detail/ <int:id>',
        }

        return Response(api_urls)

    @api_view(['GET'])
    def showAll(request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def viewProduct(request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

    @api_view(['POST'])
    def createProduct(request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    @api_view(['POST'])
    def updateProduct(request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    @api_view(['GET'])
    def deleteProduct(request, pk):
        product = Product.objects.get(id=pk)
        product.delete()

        return Response('Items deleted successfully')


class CategoryList(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    @api_view(['GET'])
    def apiOverview(request):
        api_urls = {
            'List': '/category-list/',
            'Details View': '/category-detail/<int:id>',
            'Create': '/category-create/',
            'Update': 'category-update/<int:id>',
            'Delete': '/category-detail/ <int:id>',
        }

        return Response(api_urls)

    @api_view(['GET'])
    def showAll(request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def viewCategory(request, pk):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(category, many=False)
        return Response(serializer.data)

    @api_view(['POST'])
    def createCategory(request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    @api_view(['POST'])
    def updateCategory(request, pk):
        category = Category.objects.get(id=pk)
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    @api_view(['GET'])
    def deleteCategory(request, pk):
        category = Category.objects.get(id=pk)
        category.delete()

        return Response('Items deleted successfully')


class SellerList(ModelViewSet):
    @api_view(['GET'])
    def apiOverview(request):
        api_urls = {
            'List': '/seller-list/',
            'Details View': '/sellerdetail/<int:id>',
            'Create': '/seller-create/',
            'Update': 'seller-update/<int:id>',
            'Delete': '/seller-detail/ <int:id>',
        }

        return Response(api_urls)

    @api_view(['GET'])
    def showAll(request):
        seller = Seller.objects.all()
        serializer = CategorySerializer(seller, many=True)
        return Response(serializer.data)

    @api_view(['GET'])
    def viewSeller(request, pk):
        seller = Seller.objects.get(id=pk)
        serializer = CategorySerializer(seller, many=False)
        return Response(serializer.data)


    @api_view(['POST'])
    def createSeller(request):
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


    @api_view(['POST'])
    def updateSeller(request, pk):
        seller = Seller.objects.get(id=pk)
        serializer = SellerSerializer(instance=seller, data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    @api_view(['GET'])
    def deleteSeller(request, pk):
        seller = Category.objects.get(id=pk)
        seller.delete()

        return Response('Items deleted successfully')


