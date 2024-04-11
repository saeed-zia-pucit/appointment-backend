from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorProfileViewSet(viewsets.ViewSet):
    def list(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def get_doctors_by_specialty(self, request, specialization=None):
        # Endpoint for retrieving doctors by specialty
        print("get_doctors_by_specialty()")
        if specialization:
            doctors = Doctor.objects.filter(specialization=specialization)  # Corrected the filtering criteria
            serializer = DoctorSerializer(doctors, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Specialization parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        
    def create(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            doctor = Doctor.objects.get(pk=pk)
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data)
        except Doctor.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        try:
            doctor = Doctor.objects.get(pk=pk)
            serializer = DoctorSerializer(doctor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Doctor.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            doctor = Doctor.objects.get(pk=pk)
            doctor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Doctor.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)