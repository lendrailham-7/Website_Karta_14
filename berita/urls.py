from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_berita, name='daftar_berita'),
    path('<int:id>/', views.detail_berita, name='detail_berita'),
]