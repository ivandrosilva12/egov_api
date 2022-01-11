from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.utils import timezone

# Create your models here.
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import slugify
from django.forms import modelformset_factory

from commom.models import County
from company.models import Company

from authentication.models import User

# Single
# Familiar
# Suite Master
# ...

class RoomType(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50,
        help_text="Tipo de quarto.")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tipoquarto', kwargs={'id' : self.pk})

    def get_rooms(self):
        return self.room_set.all()

    class Meta:
        ordering = ['name']
        verbose_name = 'Tipo de Quarto'
        verbose_name_plural = 'Tipos de Quartos'

# As categorias podem estar divididas em:
# Hotel
# Pensao
# Residencial
# Hospedaria  
# Guest house

class Category(models.Model):
    name = models.CharField(
        unique=True,
        max_length=50,
        help_text="Categoria.")

    def __str__(self):
        return self.name

    def get_imoveis(self):
        return self.imovel_set.all()

    def get_absolute_url(self):
        return reverse('categoria', kwargs={'id' : self.pk})

    class Meta:
        ordering = ['name']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

# Adicionar geolocation
# Alterar do modelo para Imóvel.

class Imovel(models.Model):
    name = models.CharField(
        max_length=50,
        help_text='Nome da unidade hoteleira.')
    description = models.TextField(
        help_text='Outros dados sobre a unidade hoteleira')
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    county_id = models.ForeignKey(County, on_delete=models.PROTECT)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    is_active = models.BooleanField()
    users = models.ManyToManyField(User, through='ImovelWorkers', related_name='imoveis')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('imovel', kwargs={'id' : self.pk})

    def get_users(self):
        return self.users.all()

    def get_rooms(self):
        return self.room_set.all()

    class Meta:
        ordering = ['name', 'company_id']
        unique_together = ['name', 'company_id', 'county_id']
        verbose_name = 'Imovel'
        verbose_name_plural = 'Imoveis'


class Room(models.Model):

    room_no = models.CharField(
        max_length=10,
        unique=True,
        help_text='Numero do quarto')
    room_type_id = models.ForeignKey(
        RoomType,
        null=False,
        blank=True,
        on_delete=models.PROTECT)
    imovel_id = models.ForeignKey(
        Imovel,
        null=False,
        blank=True,
        on_delete=models.CASCADE)
    description = models.TextField()
    current_price = models.DecimalField(
        max_digits = 10,
        decimal_places = 2)
    availability = models.BooleanField(
        default=False)

    def get_roomImages(self):
        return self.roomImage_set.all()

    def get_reservations(self):
        return self.reservation_set.all()


    class Meta:
        ordering = ['imovel_id', 'room_no']
        verbose_name = 'Room'
        verbose_name_plural = 'Rooms'


# Rever as dimensoes da imagem e o local de armazenamento

class RoomImage(models.Model):
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE)

    #############################################################
    # As imagens deverao ser salvas no Cloudinary ou o S3 da AWS#
    #############################################################
    image = models.ImageField(upload_to="room_img/%Y/%m/%d",
                              verbose_name='Room Picture',
                              null=True, blank=True,
                              width_field="width_field",
                              height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)


class ImovelWorkers(models.Model):

    USER_TYPE_CHOICES = (
      (1, 'manager'),
      (2, 'worker')
    )

    user_profile = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
