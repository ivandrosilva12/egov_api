from django.test import SimpleTestCase
from django.urls import reverse, resolve
from commom.views import ProvinceListView, ProvinceDetailView, CountyListView, CountyDetailView

# Create your tests here
class TestUrls(SimpleTestCase):

    def test_county_list_url_is_resolves(self):
        url = reverse('counties')
        self.assertEquals(resolve(url).func.view_class, CountyListView)

    def test_county_detail_url_is_resolves(self):
        url = reverse('county', args=[1])
        self.assertEquals(resolve(url).func.view_class, CountyDetailView)

    def test_province_list_url_is_resolves(self):
        url = reverse('provinces')
        self.assertEquals(resolve(url).func.view_class, ProvinceListView)

    def test_province_detail_url_is_resolves(self):
        url = reverse('province', args=[1])
        self.assertEquals(resolve(url).func.view_class, ProvinceDetailView)
