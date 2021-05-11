from rest_framework.serializers import ModelSerializer
from .models import PerformerModel


class PerformerSerializer(ModelSerializer):
    class Meta:
        model = PerformerModel
        fields = ['id', 'email', 'todo']
        extra_kwargs = {
            'todo': {'read_only': True}
        }
