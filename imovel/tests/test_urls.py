from django.test import SimpleTestCase
from django.urls import reverse, resolve
from imovel.views import ImovelListView, ImovelDetailView, ImovelWorkersDetailView, ImovelWorkersListView, RoomCategoryDetailView, RoomCategoryListView, RoomDetailView, RoomImageDetailView, RoomImageListView, RoomListView, RoomTypeDetailView, RoomTypeListView
# Create your tests here
class TestUrls(SimpleTestCase):

    def test_room_types_list_url_resolves(self):
        url = reverse('room_types')
        self.assertEquals(resolve(url).func.view_class, RoomTypeListView)

    def test_room_types_detail_url_resolves(self):
        url = reverse('room_type', args=[1])
        self.assertEquals(resolve(url).func.view_class, RoomTypeDetailView)

    def test_room_categories_list_url_resolves(self):
        url = reverse('room_categories')
        self.assertEquals(resolve(url).func.view_class, RoomCategoryListView)

    def test_room_categories_detail_url_resolves(self):
        url = reverse('room_category', args=[1])
        self.assertEquals(resolve(url).func.view_class, RoomCategoryDetailView)

    def test_imovel_list_url_resolves(self):
        url = reverse('imoveis')
        self.assertEquals(resolve(url).func.view_class, ImovelListView)

    def test_imovel_detail_url_resolves(self):
        url = reverse('imovel', args=[1])
        self.assertEquals(resolve(url).func.view_class, ImovelDetailView)

    def test_rooms_list_url_resolves(self):
        url = reverse('rooms')
        self.assertEquals(resolve(url).func.view_class, RoomListView)

    def test_rooms_detail_url_resolves(self):
        url = reverse('room', args=[1])
        self.assertEquals(resolve(url).func.view_class, RoomDetailView)

    def test_room_images_list_url_resolves(self):
        url = reverse('room_images')
        self.assertEquals(resolve(url).func.view_class, RoomImageListView)

    def test_room_images_detail_url_resolves(self):
        url = reverse('room_image', args=[1])
        self.assertEquals(resolve(url).func.view_class, RoomImageDetailView)

    def test_imovelworkers_list_url_resolves(self):
        url = reverse('imovelworkers')
        self.assertEquals(resolve(url).func.view_class, ImovelWorkersListView)

    def test_imovelworkers_detail_url_resolves(self):
        url = reverse('imovelworker', args=[1])
        self.assertEquals(resolve(url).func.view_class, ImovelWorkersDetailView)
