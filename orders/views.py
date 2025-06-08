from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    """
    List all orders or create a new order with order items.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete an order and its items.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
