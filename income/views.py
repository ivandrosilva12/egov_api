from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from django_filters.rest_framework import DjangoFilterBackend

from django_filters import rest_framework
from income.models import Income
from .serializers import IncomeSerializer
from rest_framework import permissions, filters
from .permissions import IsOwner


class IncomeListAPIView(ListCreateAPIView):

    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends=[rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'source']
    search_fields = ['id', 'source']
    ordering_fields = ['id', 'source']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class IncomeDetailAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = IncomeSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Income.objects.all()
    lookup_field = "id"

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
