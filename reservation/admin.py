from django.contrib import admin
from reservation.models import CheckIn, CheckOut, Reservation

# Register your models here.
admin.site.register(Reservation)
admin.site.register(CheckIn)
admin.site.register(CheckOut)
