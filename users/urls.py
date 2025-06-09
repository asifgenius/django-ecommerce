from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserListAPIView, UserRegistrationAPIView, LoginTokenObtainPairView

urlpatterns = [
    path('token/', LoginTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('', UserListAPIView.as_view(), name='user-list'),
]
