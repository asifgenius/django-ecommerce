from rest_framework import generics
from .models import Category, Product, ProductImage
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CategorySerializer, ProductSerializer, ProductImageSerializer
from .filters import ProductFilter  

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
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

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
