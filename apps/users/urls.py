from django.urls import path, include
from .views import ListCreateView, ReadUpdateDeleteView, TodoListCreateView

urlpatterns = [
    path('', ListCreateView.as_view(), name='users_get'),
    path('/<int:pk>', ReadUpdateDeleteView.as_view(), name='users_get_patch_delete'),
    path('/<int:pk>/todo', TodoListCreateView.as_view(), name='users_todo_create'),
]
