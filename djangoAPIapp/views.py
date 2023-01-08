from django.shortcuts import render
from rest_framework import generics
from .models import Category ,Book,Product
from .serializers import categoryserializer,bookserializer,productserializer
# Create your views here.


class ListCategory(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = categoryserializer


class Detailcategory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = categoryserializer

class ListBook(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = bookserializer

class DetailBook(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = bookserializer

class ListProduct(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = productserializer

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = productserializer

