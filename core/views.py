from django.shortcuts import render
from berita.models import Berita


def home(request):

    berita_terbaru = Berita.objects.order_by('-tanggal')[:3]

    context = {
        'berita_terbaru': berita_terbaru
    }

    return render(request, 'core/home.html', context)