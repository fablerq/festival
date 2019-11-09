from rest_framework import serializers
from .models import User, Profile
#from drf_role.serializers import RoleSerializer
from django.contrib.auth.models import User
from drf_role.models import *

class UserSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='role-detail',
    #     lookup_field='role'
    # )

    class Meta:
        model = User
        depth = 1
        fields = ('date_joined', 'last_login', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        depth = 1
        fields = '__all__'


