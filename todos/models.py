from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    detail = models.TextField()
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE, null = True, related_name= 'user_id')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title