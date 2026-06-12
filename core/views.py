from django.shortcuts import render
from berita.models import Berita
from agenda.models import Agenda


def home(request):

    berita_terbaru = Berita.objects.order_by(
        '-tanggal'
    )[:3]

    agenda_terdekat = Agenda.objects.order_by(
        'tanggal',
        'waktu'
    )[:3]

    return render(

        request,

        'core/home.html',

        {

            'berita_terbaru': berita_terbaru,

            'agenda_terdekat': agenda_terdekat

        }

    )