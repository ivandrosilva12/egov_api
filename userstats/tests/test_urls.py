from django.test import SimpleTestCase
from django.urls import reverse, resolve
from userstats.views import ExpenseSummaryStats

# Create your tests here
class TestUrls(SimpleTestCase):

    def test_county_list_url_is_resolves(self):
        url = reverse('expense-category-summary')
        self.assertEquals(resolve(url).func.view_class, ExpenseSummaryStats)
