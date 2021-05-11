from rest_framework.serializers import ModelSerializer
from .models import TodoModel
from ..performers.serializers import PerformerSerializer


class TodoCreateSerializer(ModelSerializer):
    performers = PerformerSerializer(many=True, required=False)

    class Meta:
        model = TodoModel
        fields = ['id', 'title', 'body', 'performers', 'user', 'created', 'updated']
        extra_kwargs = {
            'user': {'read_only': True}
        }


class TodoDetailSerializer(ModelSerializer):
    performers = PerformerSerializer(many=True, required=False)

    class Meta:
        model = TodoModel
        fields = ['id', 'title', 'body', 'performers', 'user', 'avatar', 'created', 'updated']
        extra_kwargs = {
            'user': {'read_only': True}
        }
