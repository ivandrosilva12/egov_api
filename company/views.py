from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters import rest_framework
from rest_framework import permissions, filters
from .models import Company, InvoiceCompany, CompanyUsers
from .serializers import CompanySerializer, InvoiceCompanySerializer, CompanyUsersSerializer

class CompanyListView(ListCreateAPIView):

    serializer_class = CompanySerializer
    queryset = Company.objects.all()
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


class CompanyDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Company.objects.all()
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


class InvoiceCompanyListView(ListCreateAPIView):

    serializer_class = InvoiceCompanySerializer
    queryset = InvoiceCompany.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['invoice_code']
    search_fields = ['invoice_code']
    ordering_fields = ['invoice_code']

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')


class InvoiceCompanyDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = InvoiceCompanySerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = InvoiceCompany.objects.all()
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


class CompanyUsersListView(ListCreateAPIView):

    serializer_class = CompanyUsersSerializer
    queryset = CompanyUsers.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['company']
    search_fields = ['company']
    ordering_fields = ['company']

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')


class CompanyUsersDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = CompanyUsersSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CompanyUsers.objects.all()
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
