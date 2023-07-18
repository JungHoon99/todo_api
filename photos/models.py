from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images")
    user_id = models.ForeignKey("users.User", on_delete=models.CASCADE, null = True, related_name= 'photo_user_id')
    update_time = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title