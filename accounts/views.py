from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from storefront.response  import StandardResponse
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return StandardResponse.created(successMessage="User Register Successfully",data=serializer.data)
        else:
            error_message = ""
            for field, messages in serializer.errors.items():
                error_message += f"{field}: {', '.join(messages)}. "
            return StandardResponse.error(error_message)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            try:
                # Check if the user has an associated authentication token
                if hasattr(request.user, 'auth_token') and request.user.auth_token:
                    # Delete the user's token to logout
                    request.user.auth_token.delete()
                    return StandardResponse.success(successMessage="User Logout Successfully")
                else:
                    return StandardResponse.error(error_message="User does not have an authentication token")
            except Exception as e:
                # Convert the exception to a string or provide a custom error message
                return StandardResponse.error("exception")
        else:
            return StandardResponse.error(error_message="User is not authenticated", status_code=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
 
        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            print(token.key)
            return StandardResponse.success(successMessage="Login Success",data={'token': token.key})

        return StandardResponse.error(error_message='Invalid credentials', status_code=status.HTTP_401_UNAUTHORIZED)        

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request, pk):
    try:
        user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return StandardResponse.error("User not found", status_code=status.HTTP_404_NOT_FOUND)
    
    user.delete()
    return StandardResponse.success("User Deleted Successfully",status_code=status.HTTP_204_NO_CONTENT)    