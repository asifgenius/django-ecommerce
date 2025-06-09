from rest_framework.generics import CreateAPIView, ListAPIView
from .models import User
from .serializers import UserSerializer, LoginTokenObtainPairSerializer
from django_filters.rest_framework import DjangoFilterBackend
 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,)

# Create your views here.
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'email', 'address']

class UserRegistrationAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginTokenObtainPairView(TokenObtainPairView):
    serializer_class = LoginTokenObtainPairSerializer
