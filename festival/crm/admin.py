from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile, User, Coordinate

admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Coordinate)
