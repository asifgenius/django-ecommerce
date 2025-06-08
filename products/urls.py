from django.urls import path
from . import views

urlpatterns = [
    # Category Endpoints
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),

    # Product Endpoints
    path('', views.ProductListCreateView.as_view(), name='product-list-create'),  # <-- no 'products/' here
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),

    # Product Image Endpoints
    path('images/', views.ProductImageListCreateView.as_view(), name='productimage-list-create'),
    path('images/<int:pk>/', views.ProductImageDetailView.as_view(), name='productimage-detail'),
]