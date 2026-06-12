from django.urls import path
from . import views

urlpatterns = [
    path('', views.daftar_agenda, name='daftar_agenda'),
    path('<int:id>/', views.detail_agenda, name='detail_agenda'),
]