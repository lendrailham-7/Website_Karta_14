from django.shortcuts import render
from berita.models import Berita
from agenda.models import Agenda
from pengurus.models import Pengurus


def home(request):
    berita_terbaru = Berita.objects.order_by('-tanggal')[:3]
    agenda_terdekat = Agenda.objects.order_by('tanggal', 'waktu')[:3]

    jabatan_order = [
        'Ketua',
        'Sekretaris',
        'Bendahara',
        'Ketua Pelaksana',
        'Wakil Ketua Pelaksana',
        'Acara'
        'Logistik',
        'Konsumsi',
        'Humas',
        'Sponsorship'
        'PDD',
    ]

    kepengurusan = []

    for jabatan in jabatan_order:
        anggota = Pengurus.objects.filter(
            jabatan__iexact=jabatan
        ).order_by('urutan')

        kepengurusan.append({
            'jabatan': jabatan,
            'anggota': anggota,
        })

    return render(
        request,
        'core/home.html',
        {
            'berita_terbaru': berita_terbaru,
            'agenda_terdekat': agenda_terdekat,
            'kepengurusan': kepengurusan,
        }
    )