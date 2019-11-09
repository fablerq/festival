from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]


# from django.conf.urls import url
#
# from .views import *
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path(r'users/', views.UserView.as_view()),
#    # path('users/<int:pk>/', views.UserDetailView.as_view()),
# ]