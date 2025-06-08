from rest_framework import serializers
from .models import Category, Product, ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'code',
            'category',
            'category_id',
            'slug',
            'description',
            'price',
            'sale_price',
            'created_at',
            'updated_at',
            'images',
        ]
