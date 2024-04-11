from rest_framework import serializers
from .models import Company
from .models import Employee
from rest_framework import serializers
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'founded_date']

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"



     
