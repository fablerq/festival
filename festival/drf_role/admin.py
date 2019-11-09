from django.contrib import admin
from .models import *

admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(AccessControl)
