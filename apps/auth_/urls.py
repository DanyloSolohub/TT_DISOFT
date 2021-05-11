from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from .views import RegisterView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token'),
    path('/refresh', TokenRefreshView.as_view(), name='refresh'),
    path('/register', RegisterView.as_view(), name='register')
]