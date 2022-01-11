from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from authentication.models import User
from django.utils import timezone

# Create your models here.
from django.urls import reverse

from commom.models import County

import uuid


class Company(models.Model):
    name = models.CharField(
        unique=True,
        max_length=255,
        help_text="Nome da empresa.")
    nif = models.CharField(
        max_length=15,
        unique=True,
        help_text='NIF da empresa.')
    email = models.EmailField(
        unique=True,
        help_text='E-mail da empresa.')
    phone = models.CharField(
        max_length=9,
        unique = True,
        null = False,
        blank = False,
        help_text='Contacto telefónico.')
    county_id = models.ForeignKey(County, on_delete=models.PROTECT)
    company_address = models.CharField(
        max_length=255,
        help_text='Morada da empresa.')
    details = models.TextField(
        help_text='Outros dados da empresa.')
    is_active = models.BooleanField(default=True)
    users = models.ManyToManyField(User, through='CompanyUsers', related_name='companies')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company', kwargs={'id' : self.pk})

    def get_imoveis(self):
        return self.imovel_set.all()

    def get_invoices(self):
        return self.invoiceCompany_set.all()
        
    def get_company_users(self):
        return self.users.all()

    def deassociate_users(self):
        return self.users.clear()

    def deassociate_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            return self.users.remove(user)
        except User.DoesNotExist:
            print('User is not associated to this company')

    def add_user(self, user):      
        self.users.add(user)
        return self.users

    def add_users(self, new_users):
        for user in new_users:
            self.users.add(user)
        return self.users

    def deactivate_company(self):
        self.is_active = False
        return self.is_active

    def activate_company(self):
        self.is_active = True
        return self.is_active

    class Meta:
        ordering = ['name', 'county_id', 'nif']
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class InvoiceCompany(models.Model):

    invoice_code = models.UUIDField(
        default=uuid.uuid4,
        editable=False)
    company_id = models.ForeignKey(
        Company,
        on_delete=models.CASCADE)
    invoice_amount = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        help_text="Valor total a receber.")
    start_date = models.DateField(
        null=False,
        blank=False,
        help_text='Data de início')
    end_date = models.DateField(
        null=False,
        blank=False,
        help_text='Data de fim')
    invoice_details = models.TextField(
        help_text='Detalhes da fatura')
    ts_issued = models.DateTimeField(default=timezone.now)
    ts_paid = models.DateTimeField(null=False, blank=True)
    ts_canceled = models.DateTimeField()

    def __str__(self):
        return 'Invoice {} from {} company, from {} to {}'.format(
            self.invoice_code,
            self.company_id,
            self.start_date,
            self.end_date)

    def get_absolute_url(self):
        return reverse('invoicecompany', kwargs={'id' : self.pk})

    class Meta:
        ordering = ['-ts_issued', 'company_id']
        verbose_name = 'Invoicecompany'
        verbose_name_plural = 'Invoicecompanies'


class CompanyUsers(models.Model):

    USER_TYPE_CHOICES = (
      (1, 'owner'),
      (2, 'manager'),
      (3, 'worker'),
    )

    user_profile = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('companyusers', kwargs={'id' : self.pk})

    def __str__(self):
        return '{} from {} company'.format(
            self.company,
            self.user)

    class Meta:
        ordering = ['company', 'user']
        verbose_name = 'CompanyUser'
        verbose_name_plural = 'CompanyUsers'
