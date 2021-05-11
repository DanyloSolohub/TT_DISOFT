# Generated by Django 3.2.2 on 2021-05-10 22:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_todo', to=settings.AUTH_USER_MODEL),
        ),
    ]
