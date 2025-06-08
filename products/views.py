from rest_framework import generics
from .models import Category, Product, ProductImage
from .serializers import CategorySerializer, ProductSerializer, ProductImageSerializer

# Category Views
class CategoryListCreateView(generics.ListCreateAPIView):
    '''
    List all categories or create a new category.
    '''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''
    Get, update, or delete a single category by ID.
    '''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Product Views
class ProductListCreateView(generics.ListCreateAPIView):
    '''
    List all products or create a new product.
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''
    Get, update, or delete a single product by ID.
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# ProductImage Views
class ProductImageListCreateView(generics.ListCreateAPIView):
    '''
    List all product images or upload a new product image.
    '''
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

class ProductImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''
    Get, update, or delete a single product image by ID.
    '''
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
