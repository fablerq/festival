from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions
from .models import User
from .serializers import UserSerializer
from rest_framework import generics, status
from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class UserView(generics.ListCreateAPIView):
#     print("enteredd")
#     #permission_classes = (IsAdminOrNoAccess,)
#     serializer_class = UserSerializer
#     queryset = User.objects.all()

# class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
#     #permission_classes = (IsAdminOrNoAccess,)
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
