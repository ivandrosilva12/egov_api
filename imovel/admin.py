from django.contrib import admin

from imovel.models import Category, Imovel, ImovelWorkers, Room, RoomImage, RoomType

# Register your models here.
admin.site.register(RoomType)
admin.site.register(Category)

admin.site.register(Imovel)
admin.site.register(Room)

admin.site.register(RoomImage)
admin.site.register(ImovelWorkers)
