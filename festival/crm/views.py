from django.shortcuts import render
from rest_framework import viewsets, mixins, permissions
from rest_framework import generics, status
from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


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

@permission_classes([IsAuthenticated])
class CoordinateList(generics.ListCreateAPIView):
  #  permission_classes = (IsAuthenticated,)
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer

class CoordinateDetail(generics.RetrieveUpdateDestroyAPIView):
   # permission_classes = (IsAuthenticated,)
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer


