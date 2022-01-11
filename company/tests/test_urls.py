from django.test import SimpleTestCase
from django.urls import reverse, resolve
from company.views import CompanyListView, CompanyDetailView, InvoiceCompanyListView, InvoiceCompanyDetailView, CompanyUsersListView, CompanyUsersDetailView

# Create your tests here
class TestUrls(SimpleTestCase):

    def test_company_list_url_is_resolves(self):
        url = reverse('companies')
        self.assertEquals(resolve(url).func.view_class, CompanyListView)

    def test_company_detail_url_is_resolves(self):
        url = reverse('company', args=[1])
        self.assertEquals(resolve(url).func.view_class, CompanyDetailView)

    def test_invoice_company_list_url_is_resolves(self):
        url = reverse('invoicecompanies')
        self.assertEquals(resolve(url).func.view_class, InvoiceCompanyListView)

    def test_invoice_company_detail_url_is_resolves(self):
        url = reverse('invoicecompany', args=[1])
        self.assertEquals(resolve(url).func.view_class, InvoiceCompanyDetailView)

    def test_company_users_list_url_is_resolves(self):
        url = reverse('companyusers')
        self.assertEquals(resolve(url).func.view_class, CompanyUsersListView)

    def test_company_users_detail_url_is_resolves(self):
        url = reverse('companyuser', args=[1])
        self.assertEquals(resolve(url).func.view_class, CompanyUsersDetailView)
