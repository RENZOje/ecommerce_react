from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

urlpatterns = [
    path('users/login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register', registerUser, name='register'),

    path('users/', getUsers, name='users'),
    path('users/profile/', getUserProfile, name='users-profile'),

    path('products/', getProducts, name='products'),
    path('products/<str:pk>/', getProduct, name='product'),

]
