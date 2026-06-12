from django.shortcuts import render

from .models import Pengurus, Divisi


def daftar_pengurus(request):

    pengurus_inti = Pengurus.objects.filter(
        divisi__isnull=True
    ).order_by(
        'urutan'
    )

    divisi = Divisi.objects.prefetch_related(
        'pengurus_set'
    ).order_by(
        'urutan'
    )

    return render(

        request,

        'pengurus/daftar_pengurus.html',

        {
            'pengurus_inti': pengurus_inti,
            'divisi': divisi
        }

    )