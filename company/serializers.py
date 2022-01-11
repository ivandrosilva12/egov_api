from rest_framework import serializers
from .models import Company, InvoiceCompany, CompanyUsers

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'

class InvoiceCompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceCompany
        fields = '__all__'

class CompanyUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyUsers
        fields = '__all__'
