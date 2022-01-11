from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
#from django_filters.rest_framework import DjangoFilterBackend

from django_filters import rest_framework
from expenses.models import Expense
from .serializers import ExpenseSerializer
from rest_framework import permissions, filters
from .permissions import IsOwner


class ExpenseListAPIView(ListCreateAPIView):

    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'category']
    search_fields = ['id', 'category', 'date', 'amount']
    ordering_fields = ['id', 'category']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class ExpenseDetailAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = ExpenseSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Expense.objects.all()
    lookup_field = "id"

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
