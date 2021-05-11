import os

from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


def to_upload(instance, filename):
    return os.path.join(f'{instance.title}.{instance.user.email}', 'avatars', filename)


# Create your models here.
class TodoModel(models.Model):
    class Meta:
        db_table = 'todos'

    title = models.CharField(max_length=30)
    body = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='created_todo')
    avatar = models.ImageField(upload_to=to_upload)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
