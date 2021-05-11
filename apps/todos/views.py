from rest_framework.generics import get_object_or_404, ListAPIView, RetrieveUpdateDestroyAPIView, \
    ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from apps.performers.models import PerformerModel
from apps.performers.serializers import PerformerSerializer
from apps.todos.models import TodoModel
from apps.todos.serializers import TodoDetailSerializer
from .services import Services


class PerformerCreateView(ListCreateAPIView):
    serializer_class = PerformerSerializer

    def get_permissions(self):
        todo_id = self.kwargs.get('pk')
        todo = get_object_or_404(TodoModel, pk=todo_id)
        pk = todo.user.id
        if self.request.user.id != pk:
            return [IsAdminUser()]
        return [IsAuthenticated()]

    def get_queryset(self):
        todo_id = self.kwargs.get('pk')
        return PerformerModel.objects.filter(todo_id=todo_id)

    def perform_create(self, serializer):
        todo_id = self.kwargs.get('pk')
        todo = get_object_or_404(TodoModel, pk=todo_id)
        serializer.save(todo=todo)

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        todo_id = self.kwargs.get('pk')
        todo = get_object_or_404(TodoModel, pk=todo_id)
        data = {
            'subject': 'Your todo',
            'body': f'{todo.title} \n'
                    f'{todo.body}',
            'to': [email]
        }
        Services.send_mail(**data)
        return super().create(request, *args, **kwargs)


class ReadUpdateDeleteTodoView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoDetailSerializer
    queryset = TodoModel.objects.all()

    def get_permissions(self):
        todo_id = self.kwargs.get('pk')
        todo = get_object_or_404(TodoModel, pk=todo_id)
        pk = todo.user.id
        if self.request.user.id != pk:
            return [IsAdminUser()]
        return [IsAuthenticated()]


class ListTodoView(ListAPIView):
    serializer_class = TodoDetailSerializer
    queryset = TodoModel.objects.all()
