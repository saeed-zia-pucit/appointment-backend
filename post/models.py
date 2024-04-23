from django.db import models
from django.core.validators import MaxValueValidator
from accounts.models import CustomUser

class SocialMediaPost(models.Model):  
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1) 
    content = models.TextField()  
    likes = models.PositiveIntegerField(default=0)  
    comments = models.PositiveIntegerField(default=0)  
    image = models.ImageField(upload_to='social_media_images/', null=True, blank=True)  

    def __str__(self):
        return f"Post by {self.user.username}"  