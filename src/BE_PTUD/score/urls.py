from django.urls import path
from . import views

urlpatterns = [
    path('GetDanhSachDiem', views.GetDanhSachDiem.as_view(), name = 'GetDanhSachDiem'),
    path('AddDiem', views.AddDiem.as_view(), name = 'AddDiem'),
    path('UpdateDiem', views.UpdateDiem.as_view(), name = 'UpdateDiem'),
]