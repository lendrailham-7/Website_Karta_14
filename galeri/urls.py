from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_galeri, name='daftar_galeri'),
    path('<int:id>/', views.detail_galeri, name='detail_galeri'),
]