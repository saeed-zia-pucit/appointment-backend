from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    username = models.CharField(max_length = 30,unique = True)
    password = models.CharField(max_length = 20)
   

    def __str__(self):
        return self.username