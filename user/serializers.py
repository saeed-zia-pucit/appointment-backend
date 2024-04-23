from rest_framework import serializers
from .models import Doctor

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'