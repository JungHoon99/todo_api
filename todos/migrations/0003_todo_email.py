# Generated by Django 4.2.3 on 2023-07-07 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('todos', '0002_alter_todo_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='email',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publisher', to='users.user'),
        ),
    ]
