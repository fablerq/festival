from django.db import models
from drf_role.models import Role
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
#from django.contrib.auth.models import User
from django.db.models.signals import post_save


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=50)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return "{}".format(self.email)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=255, default="Unknown")
    last_name = models.CharField(max_length=255,default="Unknown")
    phone = models.CharField(max_length=255,default="Unknown")
    email = models.EmailField(unique=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

