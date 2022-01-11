from django.urls import path
from .import views

urlpatterns = [
    path('reservations/', views.ReservationListView.as_view(), name="reservations"),
    path('reservations/<int:id>', views.ReservationDetailView.as_view(), name="reservation"),
    path('checkins/', views.CheckInListView.as_view(), name="checkins"),
    path('checkins/<int:id>', views.CheckInDetailView.as_view(), name="checkin"),
    path('checkouts/', views.CheckOutListView.as_view(), name="checkouts"),
    path('checkouts/<int:id>', views.CheckOutDetailView.as_view(), name="checkout"),
]
