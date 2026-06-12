from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.daftar_pengurus,
        name='daftar_pengurus'
    ),
    

]