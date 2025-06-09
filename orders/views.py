from rest_framework import generics
from .models import Order, User
from .serializers import OrderCreateUpdateSerializer,OrderSerializer
from rest_framework.permissions import IsAuthenticated

class OrderListCreateView(generics.ListCreateAPIView):
    """
    List all orders or create a new order with order items.
    """
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = User.objects.get(id=self.request.user.id)
        return Order.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return OrderCreateUpdateSerializer
        return OrderSerializer

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete an order and its items.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return OrderCreateUpdateSerializer
        return OrderSerializer
