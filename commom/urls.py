from django.urls import path
from .import views

urlpatterns = [
    path('provinces/', views.ProvinceListView.as_view(), name="provinces"),
    path('provinces/<int:id>', views.ProvinceDetailView.as_view(), name="province"),
    path('counties/', views.CountyListView.as_view(), name="counties"),
    path('counties/<int:id>', views.CountyDetailView.as_view(), name="county"),
]
