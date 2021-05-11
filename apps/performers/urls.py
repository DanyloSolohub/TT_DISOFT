from django.urls import path
from .views import ListView, ReadUpdateDeleteAPIView

urlpatterns = [
    path('', ListView.as_view()),
    path('/<int:pk>', ReadUpdateDeleteAPIView.as_view())
]
