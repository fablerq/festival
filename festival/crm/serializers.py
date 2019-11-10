from rest_framework import serializers
from .models import *
from drf_role.models import *
from django.db import transaction
from django.contrib.auth.hashers import make_password, check_password
import datetime
from django.http import JsonResponse


class CoordinateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coordinate
        depth = 1
        fields = '__all__'

    def create(self, validated_data):
        user = self.context.get('request').user
        Coordinate.objects.create(
            longitude = self.data.get('longitude'),
            latitude = self.data.get('latitude'),
            time = datetime.datetime.now(),
            user_id = user.id
        )
        return JsonResponse({'status':'Success'}, status=200)


class UserSerializer(serializers.ModelSerializer):

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
            hashed_pwd = make_password(password)
            User.objects.create(
                email=email, password=hashed_pwd,
            )
            #found_role = Role.objects.filter(type=0).first()
            found_user = User.objects.filter(email=email).first()
            created_profile = Profile.objects.create(
                password=hashed_pwd,
                user = found_user,
                status = validated_data.pop('status'),
                first_name=validated_data.pop('first_name'),
                last_name=validated_data.pop('last_name'),
                phone=validated_data.pop('phone'),
                email=email,
            )
            created_profile.roles.add(Role.objects.filter(type=0).first())
            return created_profile

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        depth = 1
        fields = '__all__'

class EventTimetableSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventTimetable
        depth = 1
        fields = '__all__'

class MapBorderSerializer(serializers.ModelSerializer):

    class Meta:
        model = MapBorder
        depth = 1
        fields = '__all__'