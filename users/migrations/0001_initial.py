# Generated by Django 4.2.3 on 2023-07-07 12:25

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100, validators=[users.validators.email_validate])),
                ('pw', models.CharField(max_length=50, validators=[users.validators.password_validate])),
                ('phone', models.CharField(max_length=15, validators=[users.validators.phone_number_validate])),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
