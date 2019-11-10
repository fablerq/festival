from rest_framework import serializers
from .models import User, Profile
#from drf_role.serializers import RoleSerializer
#from django.contrib.auth.models import User
from drf_role.models import *
from django.db import transaction
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.contrib.auth.hashers import make_password, check_password

class UserSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='role-detail',
    #     lookup_field='role'
    # )

    class Meta:
        model = User
        depth = 1
        fields = ('id', 'date_joined', 'last_login', 'email')



class ProfileSerializer(serializers.ModelSerializer):
   # user = UserSerializer()
    class Meta:
        model = Profile
        depth = 1
        fields = '__all__'


    def create(self, validated_data):
        with transaction.atomic():
            email = validated_data.pop('email')
            password = validated_data.pop('password')
            # sha_signature = PBKDF2PasswordHasher.encode(password)
            hashed_pwd = make_password(password)
            User.objects.create(
                email=email, password=hashed_pwd, is_superuser=1, is_staff=1
            )
            found_role = Role.objects.filter(type=0).first()
            found_user = User.objects.filter(email=email).first()
            created_profile = Profile.objects.create(
                user = found_user,
                role= found_role,
                first_name=validated_data.pop('first_name'),
                last_name=validated_data.pop('last_name'),
                phone=validated_data.pop('phone'),
                email=email,
            )
            return created_profile

