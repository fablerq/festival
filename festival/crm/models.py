from django.db import models
from drf_role.models import Role
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
#from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.postgres.fields import ArrayField


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return "{}".format(self.email)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    roles = models.ManyToManyField(Role)
    first_name = models.CharField(max_length=255, default="Unknown")
    last_name = models.CharField(max_length=255,default="Unknown")
    phone = models.CharField(max_length=255,default="Unknown")
    email = models.EmailField(unique=True, null=True)
    password = models.CharField(max_length=255, default='qwerty')
    status = models.CharField(max_length=255, default='Не подтвержден')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Coordinate(models.Model):
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    time = models.DateTimeField(null=True)
    user_id = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.longitude} {self.latitude}, {self.time}"

class Event(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    sub_titles = ArrayField(models.CharField(max_length=200), default=list)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True)

class EventTimetable(models.Model):
    date = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null= True)

class MapBorder(models.Model):
    title = models.CharField(max_length=200)
    color = models.CharField(max_length=100)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null= True)
    coordinates = ArrayField(models.CharField(max_length=200), default=list)
