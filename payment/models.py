from django.db import models
from django.db.models.deletion import CASCADE
from authentication.models import User
from django.utils import timezone

# Create your models here.

from reservation.models import Reservation


class Invoice(models.Model):
    guest_id = models.ForeignKey(User, on_delete=CASCADE)
    reservation_id = models.ForeignKey(Reservation, on_delete=CASCADE)
    invoice_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    paid_at=models.DateTimeField(auto_now_add=True)
    canceled_at=models.DateTimeField(auto_now=True)



### Criar a classe Payment