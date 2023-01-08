from rest_framework import serializers
from .models import Category,Book,Product

class categoryserializer(serializers.ModelSerializer):
    class meta:
        filed = (
            'id'
            'title',
        )
        model =Category

class bookserializer(serializers.ModelSerializer):
    class meta:
        filed = (
            'id'
            'title',
            'Category',
            'isbn',
            'pages',
            'price',
            'stock',
            'description',
            'imageUrl',
            'status',
            'data_created',

        )
        model =Book

class productserializer(serializers.ModelSerializer):
    class meta:
        filed = (
            'id'
            'product_tage',
            'name',
            'Category',
            'price',
            'stock',
            'imageUrl',
            'status',
            'data_created',
            'description',
            'qte',

        )
        model =Product


