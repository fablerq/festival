from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions
from .models import User
from .serializers import UserSerializer
from rest_framework import generics, status
from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView


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

# class ProfileCreate(APIView):
#     def post(self, request, format=None):
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
