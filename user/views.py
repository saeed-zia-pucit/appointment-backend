from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from storefront.response import StandardResponse
from .models import User

class UserProfileViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return StandardResponse.success(success_message="User Register Successfully", data=serializer.data)
             
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return StandardResponse.error("User not found")
        
        user.delete()
        return StandardResponse.success("User Deleted Successfully")

    def user_logout(self, request):
        if request.user.is_authenticated:
            try:
                if hasattr(request.user, 'auth_token') and request.user.auth_token:
                    request.user.auth_token.delete()
                    return StandardResponse.success(successMessage="User Logout Successfully")
                else:
                    return StandardResponse.error(error_message="User does not have an authentication token")
            except Exception as e:
                return StandardResponse.error("exception")
        else:
            return StandardResponse.error(error_message="User is not authenticated")

    def user_login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = None
        if '@' in username:
            try:
                user = User.objects.get(email=username)
            except ObjectDoesNotExist:
                pass
        if not user:
            user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return StandardResponse.success(successMessage="Login Success",data={'token': token.key})
        return StandardResponse.error(error_message='Invalid credentials')