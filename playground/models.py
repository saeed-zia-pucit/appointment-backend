from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    founded_date = models.DateField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.name