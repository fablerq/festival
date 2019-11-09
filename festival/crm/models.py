from django.db import models
from drf_role.models import Role
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=255, default="Unknown")
    last_name = models.CharField(max_length=255,default="Unknown")
    phone = models.CharField(max_length=255,default="Unknown")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


