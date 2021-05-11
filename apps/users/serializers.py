from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

from apps.todos.serializers import TodoDetailSerializer

UserModel = get_user_model()


class UserSerializer(ModelSerializer):
    created_todo = TodoDetailSerializer(many=True, required=False)

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'created_todo']
