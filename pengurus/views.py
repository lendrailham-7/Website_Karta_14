from django.shortcuts import render

from .models import Pengurus

def daftar_pengurus(request):

    pengurus = Pengurus.objects.order_by(
        'urutan'
    )

    return render(

        request,

        'pengurus/daftar_pengurus.html',

        {
            'pengurus': pengurus
        }

    )