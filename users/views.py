from rest_framework.generics import ListAPIView
from .models import User
from .serializers import UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
 

# Create your views here.
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'email', 'address']
