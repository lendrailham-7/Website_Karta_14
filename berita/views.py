from django.shortcuts import render, get_object_or_404
from .models import Berita


def daftar_berita(request):
    berita = Berita.objects.all().order_by('-tanggal')

    return render(
        request,
        'berita/daftar_berita.html',
        {'berita': berita}
    )


def detail_berita(request, id):
    berita = get_object_or_404(Berita, id=id)

    return render(
        request,
        'berita/detail_berita.html',
        {'berita': berita}
    )