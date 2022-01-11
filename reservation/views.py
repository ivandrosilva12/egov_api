from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters import rest_framework
from rest_framework import permissions, filters
from .models import CheckIn, CheckOut, Reservation
from .serializers import CheckInSerializer, CheckOutSerializer, ReservationSerializer


class ReservationListView(ListCreateAPIView):

    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = [
        'customer',
        'expected_arrival_date_time',
        'expected_departure_date_time',
        'status']
    search_fields = [
        'customer',
        'expected_arrival_date_time',
        'expected_departure_date_time']
    ordering_fields = [
        'customer',
        'expected_arrival_date_time',
        'expected_departure_date_time']

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Reservation.objects.all()
        else:
            return Reservation.objects.filter(customer = self.request.user)

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            raise PermissionDenied('You are not authorized')
        else:
            return serializer.save()


class ReservationDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = ReservationSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Reservation.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Reservation.objects.all()
        else:
            return Reservation.objects.filter(customer = self.request.user)

    def perform_update(self, serializer):
        if self.request.user.is_superuser:
            raise PermissionDenied('You are not authorized')
        else:
            return serializer.save()

    def perform_destroy(self, serializer):
            return serializer.save()


class CheckInListView(ListCreateAPIView):

    serializer_class = CheckInSerializer
    queryset = CheckIn.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

#    filterset_fields = ['name']
#    search_fields = ['name']
#    ordering_fields = ['name']

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')


class CheckInDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = CheckInSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CheckIn.objects.all()
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


class CheckOutListView(ListCreateAPIView):

    serializer_class = CheckOutSerializer
    queryset = CheckOut.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

#    filterset_fields = ['is_active', 'company_id', 'county_id', 'category_id']
#    search_fields = ['name', 'company_id', 'county_id', 'category_id']
#    ordering_fields = ['name', 'company_id', 'county_id', 'category_id']

    def perform_create(self, serializer):
        if self.request.user.is_superuser:
            return serializer.save()
        else:
            raise PermissionDenied('You are not authorized')


class CheckOutDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = CheckOutSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CheckOut.objects.all()
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
