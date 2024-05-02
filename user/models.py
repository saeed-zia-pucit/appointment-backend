from django.db import models
from django.core.validators import MaxValueValidator
class User(models.Model):
    
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email