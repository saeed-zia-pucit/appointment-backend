from django.db import models
from django.core.validators import MaxValueValidator
from accounts.models import CustomUser

class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True,default = 1)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    phoneNumber = models.CharField(max_length =20)
    image = models.ImageField(upload_to='doctor_images/', null=True, blank=True)

    def __str__(self):
        return self.name
