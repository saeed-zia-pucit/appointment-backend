from django.urls import path
from .views import UserProfileViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('register/', UserProfileViewSet.as_view({'post': 'create'}), name='user-register'),
    path('logout/', UserProfileViewSet.as_view({'post': 'user_logout'}), name='user-logout'),
    path('login/', UserProfileViewSet.as_view({'post': 'user_login'}), name='user-login'),
    path('delete/<int:pk>/', UserProfileViewSet.as_view({'delete': 'destroy'}), name='user-delete'),
]
