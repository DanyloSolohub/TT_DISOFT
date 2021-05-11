from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404

from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .serializers import UserSerializer
from ..todos.models import TodoModel
from ..todos.serializers import TodoCreateSerializer

UserModel = get_user_model()


class ListCreateView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class ReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        pk = self.kwargs.get('pk')
        if self.request.user.id != pk:
            return [IsAdminUser()]
        return [IsAuthenticated()]


class TodoListCreateView(ListCreateAPIView):
    serializer_class = TodoCreateSerializer

    def perform_create(self, serializer):
        user_id = self.kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=user_id)
        serializer.save(user=user)

    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        return TodoModel.objects.filter(user=user_id)

    def get_permissions(self):
        pk = self.kwargs.get('pk')
        if self.request.user.id != pk:
            return [IsAdminUser()]
        return [IsAuthenticated()]
