from rest_framework import serializers
from .models import Product, Tester, Comment
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['pid', 'name', 'category', 'makerName',
                'photoUrl', 'detailUrl']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tester
        fields = '__all__'