from django.db import models
from .validators import *

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, validators=[email_validate])
    pw = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, validators=[phone_number_validate])
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name