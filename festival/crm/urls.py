from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('coordinates/', CoordinateList.as_view()),
    path('coordinates/<int:pk>/', CoordinateDetail.as_view()),
    path('events/', EventList.as_view()),
    path('events/<int:pk>/', EventDetail.as_view()),
    path('map_borders/', MapBorderList.as_view()),
    path('map_borders/<int:pk>/', MapBorderDetail.as_view()),
    path('event_timetables/', EventTimetableList.as_view()),
    path('event_timetables/<int:pk>/', EventTimetableDetail.as_view()),
]
