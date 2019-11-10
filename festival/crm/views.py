from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions
from rest_framework import generics, status
from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    http_method_names = ['get', 'post']
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CoordinateList(generics.ListCreateAPIView):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer

class CoordinateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer


