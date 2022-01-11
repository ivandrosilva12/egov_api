from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters import rest_framework
from rest_framework import permissions, filters
from .models import Province, County
from .serializers import ProvinceSerializer, CountySerializer

class ProvinceListView(ListCreateAPIView):

    serializer_class = ProvinceSerializer
    queryset = Province.objects.all()
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


class ProvinceDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = ProvinceSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Province.objects.all()
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


class CountyListView(ListCreateAPIView):

    serializer_class = CountySerializer
    queryset = County.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['province']
    search_fields = ['name', 'province']
    ordering_fields = ['name', 'province']

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')


class CountyDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = CountySerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = County.objects.all()
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
