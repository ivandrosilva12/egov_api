from django.urls import path
from .import views

urlpatterns = [
    path('companies/', views.CompanyListView.as_view(), name="companies"),
    path('companies/<int:id>', views.CompanyDetailView.as_view(), name="company"),
    path('invoicecompanies/', views.InvoiceCompanyListView.as_view(), name="invoicecompanies"),
    path('invoicecompanies/<int:id>', views.InvoiceCompanyDetailView.as_view(), name="invoicecompany"),
    path('companyusers/', views.CompanyUsersListView.as_view(), name="companyusers"),
    path('companyusers/<int:id>', views.CompanyUsersDetailView.as_view(), name="companyuser"),
]
