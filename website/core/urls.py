from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth/acquire-token', TokenObtainPairView.as_view(), name='getToken'),
    path('auth/refresh-token', TokenRefreshView.as_view(), name='refreshToken'),
]