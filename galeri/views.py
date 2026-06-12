from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

from .models import Galeri

def daftar_galeri(request):

    galeri = Galeri.objects.order_by(
        '-tanggal'
    )

    return render(

        request,

        'galeri/daftar_galeri.html',

        {
            'galeri': galeri
        }

    )
def detail_galeri(request, id):

    galeri = get_object_or_404(
        Galeri,
        id=id
    )

    return render(

        request,

        'galeri/detail_galeri.html',

        {
            'galeri': galeri
        }

    )