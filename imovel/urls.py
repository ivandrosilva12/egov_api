from django.urls import path
from .import views

urlpatterns = [
    path('roomtypes/', views.RoomTypeListView.as_view(), name="room_types"),
    path('roomtypes/<int:id>', views.RoomTypeDetailView.as_view(), name="room_type"),
    path('categories/', views.RoomCategoryListView.as_view(), name="room_categories"),
    path('categories/<int:id>', views.RoomCategoryDetailView.as_view(), name="room_category"),
    path('imoveis/', views.ImovelListView.as_view(), name="imoveis"),
    path('imoveis/<int:id>', views.ImovelDetailView.as_view(), name="imovel"),
    path('rooms/', views.RoomListView.as_view(), name="rooms"),
    path('rooms/<int:id>', views.RoomDetailView.as_view(), name="room"),
    path('roomimages/', views.RoomImageListView.as_view(), name="room_images"),
    path('roomimages/<int:id>', views.RoomImageDetailView.as_view(), name="room_image"),
    path('imovelworkers/', views.ImovelWorkersListView.as_view(), name="imovelworkers"),
    path('imovelworkers/<int:id>', views.ImovelWorkersDetailView.as_view(), name="imovelworker"),
]
