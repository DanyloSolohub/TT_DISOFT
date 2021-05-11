from django.urls import path
from .views import PerformerCreateView, ListTodoView, ReadUpdateDeleteTodoView

urlpatterns = [
    path('', ListTodoView.as_view(), name='todos_list'),
    path('/<int:pk>', ReadUpdateDeleteTodoView.as_view(), name='users_get_patch_delete'),
    path('/<int:pk>/performer', PerformerCreateView.as_view(), name='todos_performer_create')
]
