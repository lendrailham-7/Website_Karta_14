from django.urls import path

from . import views

urlpatterns = [

    path(
        '',
        views.kontak,
        name='kontak'
    ),

]