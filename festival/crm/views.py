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

#############################################
#Coordinate
#############################################

#@permission_classes([IsAuthenticated])
class CoordinateList(generics.ListCreateAPIView):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer

#@permission_classes([IsAuthenticated])
class CoordinateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coordinate.objects.all()
    serializer_class = CoordinateSerializer

#############################################
#Event
#############################################
#@permission_classes([IsAuthenticated])
class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

#@permission_classes([IsAuthenticated])
class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

#############################################
#MapBorder
#############################################
#@permission_classes([IsAuthenticated])
class MapBorderList(generics.ListCreateAPIView):
    queryset = MapBorder.objects.all()
    serializer_class = MapBorderSerializer

#@permission_classes([IsAuthenticated])
class MapBorderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MapBorder.objects.all()
    serializer_class = MapBorderSerializer

#############################################
#EventTimetable
#############################################
#@permission_classes([IsAuthenticated])
class EventTimetableList(generics.ListCreateAPIView):
    queryset = EventTimetable.objects.all()
    serializer_class = EventTimetableSerializer

#@permission_classes([IsAuthenticated])
class EventTimetableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventTimetable.objects.all()
    serializer_class = EventTimetableSerializer