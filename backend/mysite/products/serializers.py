from rest_framework import serializers
from .models import Product, Tester, Comment

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CreateProductSerializer(serializer.ModelSerializer):
    class Meta:
        model = Product
        fields = ['pid', 'name', 'category', 'makerName',
                'photoUrl', 'detailUrl']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentProduct
        fields = '__all__'


class TesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tester
        fields = '__all__'