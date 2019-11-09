from django.db import transaction
from rest_framework import generics, status
from rest_framework.response import Response
from .utils.url_utilities import get_urls
from .models import Role, Permission, AccessControl
from .permissions import *
from .serializers import RoleSerializer, PermissionSerializer, AccessControlSerializer, AllViewListSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.views import APIView

@api_view(['GET'])
@permission_classes([IsAdminOrNoAccess])
def check_work(request):
    return Response({'key': 'value'}, status=status.HTTP_200_OK)

class RoleView(generics.ListCreateAPIView):
    #permission_classes = (IsAdminOrNoAccess,)
    serializer_class = RoleSerializer
    queryset = Role.objects.all()


class PermissionView(generics.ListCreateAPIView):
    #permission_classes = (IsAdminOrNoAccess,)
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()
    models = (Permission,)


class AccessControlView(generics.ListCreateAPIView):
    #permission_classes = (IsAdminOrNoAccess,)
    serializer_class = AccessControlSerializer
    queryset = AccessControl.objects.all()

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            permissions = request.data.get('permissions')
            permission_instance_list = [p for p in Permission.objects.filter(pk__in=permissions)]
            serializer = AccessControlSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                instance = AccessControl.objects.filter(
                    role_id=request.data.get('role'), url_name=request.data.get('url_name')
                ).first()
                if instance is None:
                    instance = serializer.save()
                if instance:
                    # First Clear all permissions
                    instance.permissions.clear()
                    # Add Permission
                    instance.permissions.add(*permission_instance_list)
                    return Response(serializer.data)
            return Response(serializer.data)


class AllUrlList(APIView):
    #permission_classes = (IsAdminOrNoAccess,)

    def get(self, request, *args, **kwargs):
        data = {
            'url_names': get_urls()  # it will be a list
        }
        serializer = AllViewListSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.validated_data)
        return serializer.data
