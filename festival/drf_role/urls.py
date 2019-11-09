from django.conf.urls import url

from .views import *
from django.urls import path
from . import views


urlpatterns = [
    path('check/', views.check_work, name='check_work'),
    url(r'^roles/', RoleView.as_view()),
    url(r'^permissions/', PermissionView.as_view()),
    url(r'^accesses/', AccessControlView.as_view()),
    url(r'^all-urls/', AllUrlList.as_view()),
]
