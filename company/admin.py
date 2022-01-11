from django.contrib import admin

from company.models import Company, InvoiceCompany, CompanyUsers

# Register your models here.
admin.site.register(Company)
admin.site.register(InvoiceCompany)
admin.site.register(CompanyUsers)