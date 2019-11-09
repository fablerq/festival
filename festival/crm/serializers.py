from rest_framework import serializers
from .models import User, Profile
#from drf_role.serializers import RoleSerializer
#from django.contrib.auth.models import User
from drf_role.models import *
from django.db import transaction


class UserSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #     view_name='role-detail',
    #     lookup_field='role'
    # )

    class Meta:
        model = User
        depth = 1
        fields = ('id', 'date_joined', 'last_login', 'email')

    def create(self, validated_data):
        print(validated_data)
        # profile_data = validated_data.pop('profile')
        #
        # password = validated_data.pop('password')
        # user = User(**validated_data)
        # user.set_password(password)
        # user.save()
        # Profile.objects.create(user=user, **profile_data)
        return user


class ProfileSerializer(serializers.ModelSerializer):
   # user = UserSerializer()
    class Meta:
        model = Profile
        depth = 1
        fields = '__all__'


    def create(self, validated_data):
        with transaction.atomic():
            email = validated_data.pop('email')
            User.objects.create(email=email)
            found_role = Role.objects.filter(type=0).first()
            found_user = User.objects.filter(email=email).first()
            print(found_user)
            created_profile = Profile.objects.create(
                user = found_user,
                role= found_role,
                first_name=validated_data.pop('first_name'),
                last_name=validated_data.pop('last_name'),
                phone=validated_data.pop('phone'),
                email=email,
            )
            return created_profile

