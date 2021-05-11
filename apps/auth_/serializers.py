from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

from apps.todos.serializers import TodoCreateSerializer

UserModel = get_user_model()


class RegisterSerializer(ModelSerializer):
    todo = TodoCreateSerializer(required=False, many=True)

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password', 'created', 'updated', 'todo']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return UserModel.objects.create_user(**validated_data)
