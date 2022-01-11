from django.core.exceptions import PermissionDenied
from django.core.checks.messages import Error
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters import rest_framework
from rest_framework import permissions, filters
from .models import Category, Imovel, ImovelWorkers, Room, RoomImage, RoomType, RoomType
from .serializers import ImovelSerializer, ImovelWorkersSerializer, RoomCategorySerializer, RoomImageSerializer, RoomSerializer, RoomTypeSerializer, RoomTypeSerializer


class RoomTypeListView(ListCreateAPIView):

    serializer_class = RoomTypeSerializer
    queryset = RoomType.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')


class RoomTypeDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = RoomTypeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = RoomType.objects.all()
    lookup_field = "id"

    def perform_update(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')

    def perform_destroy(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')


class RoomCategoryListView(ListCreateAPIView):

    serializer_class = RoomCategorySerializer
    queryset = Category.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['name']

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')


class RoomCategoryDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = RoomCategorySerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Category.objects.all()
    lookup_field = "id"

    def perform_update(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')

    def perform_destroy(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')


class ImovelListView(ListCreateAPIView):

    serializer_class = ImovelSerializer
    queryset = Imovel.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['is_active', 'company_id', 'county_id', 'category_id']
    search_fields = ['name', 'company_id', 'county_id', 'category_id']
    ordering_fields = ['name', 'company_id', 'county_id', 'category_id']

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')


class ImovelDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = ImovelSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Imovel.objects.all()
    lookup_field = "id"

    def perform_update(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')

    def perform_destroy(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')


class RoomListView(ListCreateAPIView):

    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['imovel_id', 'room_type_id', 'availability']
    search_fields = ['imovel_id']
    ordering_fields = ['imovel_id', 'room_type_id', 'availability']

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')


class RoomDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = RoomSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Room.objects.all()
    lookup_field = "id"

    def perform_update(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')

    def perform_destroy(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')


class RoomImageListView(ListCreateAPIView):

    serializer_class = RoomImageSerializer
    queryset = RoomImage.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['room']
    search_fields = ['room']
    ordering_fields = ['room']

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')


class RoomImageDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = RoomImageSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = RoomImage.objects.all()
    lookup_field = "id"

    def perform_update(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')

    def perform_destroy(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')


class ImovelWorkersListView(ListCreateAPIView):

    serializer_class = ImovelWorkersSerializer
    queryset = ImovelWorkers.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['imovel', 'user', 'user_profile']
    search_fields = ['imovel', 'user', 'user_profile']
    ordering_fields = ['imovel', 'user', 'user_profile']

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')


class ImovelWorkersDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = ImovelWorkersSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ImovelWorkers.objects.all()
    lookup_field = "id"

    def perform_update(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')

    def perform_destroy(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')
