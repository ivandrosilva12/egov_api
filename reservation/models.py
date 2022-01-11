from django.db import models
from authentication.models import User
from django.utils import timezone
from imovel.models import Room

import uuid

class Reservation(models.Model):

    STATUS_TYPE_CHOICES = (
      (1, 'Active'),
      (2, 'Canceled'),
      (3, 'Pending'),
    )

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text='Customer Name')
    no_of_adults = models.PositiveIntegerField(
        default=1,
        help_text='Number of Adult Members')
    no_of_childrens = models.PositiveIntegerField(
        default=0,
        help_text='Number of Children')
    reservation_date_time = models.DateTimeField(
        default=timezone.now,
        help_text='Reservation Date Time')
    expected_arrival_date_time = models.DateTimeField(
        default=timezone.now,
        help_text='Expected Arrival Date Time')
    expected_departure_date_time = models.DateTimeField(
        default=timezone.now,
        help_text='Expected Departure Date Time')
    discount_percent = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text='Percetagem de desconto')
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Valor total')
    updated_at=models.DateTimeField(
        auto_now=True,
        help_text='Data de actualizacao')
    room_id = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        help_text='Room id')
    status = models.PositiveSmallIntegerField(
        choices=STATUS_TYPE_CHOICES,
        default=1)
    reservation_code = models.UUIDField(
        default=uuid.uuid4,
        editable=False)

    class Meta:
        ordering = ["-id"]
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return '({0}) {1}'.format(self.reservation_code, self.customer)


# Completar estas duas classes. Customizar a classe Payment

class CheckIn(models.Model):

    checkin_code = models.UUIDField(
        default=uuid.uuid4,
        editable=False)
    reservation_id = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE)
    checkin_date_time = models.DateTimeField(
        default=timezone.now,
        help_text='Checkin Date')

    def __str__(self):
        return '({0}) {1} {2}'.format(self.checkin_code, self.reservation_id, self.checkin_date_time)


class CheckOut(models.Model):

    checkout_code = models.UUIDField(
        default=uuid.uuid4,
        editable=False)
    checkin_id = models.ForeignKey(
        CheckIn,
        on_delete=models.CASCADE)
    checkout_date_time = models.DateTimeField(
        default=timezone.now,
        help_text='Checkout Date')

    def __str__(self):
        return '({0}) {1} {2}'.format(self.checkout_code, self.checkin_id, self.checkout_date_time)
