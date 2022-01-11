from django.test import SimpleTestCase
from django.urls import reverse, resolve
from reservation.views import CheckInDetailView, CheckInListView, CheckOutDetailView, CheckOutListView, ReservationListView, ReservationDetailView
# Create your tests here
class TestUrls(SimpleTestCase):

    def test_reservations_list_url_resolves(self):
        url = reverse('reservations')
        self.assertEquals(resolve(url).func.view_class, ReservationListView)

    def test_reservations_detail_url_resolves(self):
        url = reverse('reservation', args=[1])
        self.assertEquals(resolve(url).func.view_class, ReservationDetailView)

    def test_checkins_list_url_resolves(self):
        url = reverse('checkins')
        self.assertEquals(resolve(url).func.view_class, CheckInListView)

    def test_checkins_detail_url_resolves(self):
        url = reverse('checkin', args=[1])
        self.assertEquals(resolve(url).func.view_class, CheckInDetailView)

    def test_checkouts_list_url_resolves(self):
        url = reverse('checkouts')
        self.assertEquals(resolve(url).func.view_class, CheckOutListView)

    def test_checkouts_detail_url_resolves(self):
        url = reverse('checkout', args=[1])
        self.assertEquals(resolve(url).func.view_class, CheckOutDetailView)
