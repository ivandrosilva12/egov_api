from django.db import models
from django.urls import reverse

class Province(models.Model):
    name = models.CharField(
        unique=True,
        max_length=15,
        help_text="Nome da província.")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('province', kwargs={'id' : self.pk})

    def get_counties(self):
        return self.county_set.all()

    class Meta:
        ordering = ['name']
        verbose_name = 'Province'
        verbose_name_plural = 'Provinces'


class County(models.Model):
    name = models.CharField(
        unique=True,
        max_length=20,
        help_text="Nome do município.")
    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        verbose_name="the related province")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('county', kwargs={'id' : self.pk})

    def get_imoveis(self):
        return self.imovel_set.all()

    def get_companies(self):
        return self.company_set.all()


    class Meta:
        ordering = ['name']
        verbose_name = 'County'
        verbose_name_plural = 'Counties'
        unique_together = ['name', 'province']
