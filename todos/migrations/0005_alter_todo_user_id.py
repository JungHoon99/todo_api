# Generated by Django 4.2.3 on 2023-07-07 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('todos', '0004_rename_email_todo_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='users.user'),
        ),
    ]