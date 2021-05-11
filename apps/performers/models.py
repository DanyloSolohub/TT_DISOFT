from django.db import models

from ..todos.models import TodoModel


# Create your models here.
class PerformerModel(models.Model):
    class Meta:
        db_table = 'performers'

    email = models.EmailField()
    todo = models.ForeignKey(TodoModel, on_delete=models.CASCADE, related_name='performers')
