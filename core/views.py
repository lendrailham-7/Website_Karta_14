from django.shortcuts import render
from berita.models import Berita
from agenda.models import Agenda
from pengurus.models import Divisi, Pengurus


def home(request):
    berita_terbaru = Berita.objects.order_by('-tanggal')[:3]
    agenda_terdekat = Agenda.objects.order_by('tanggal', 'waktu')[:3]

    jabatan_inti = [
        'PEMBINA',
        'MENPORA RW 14',
        'KETUA',
        'WAKIL KETUA',
        'KETUA PANITIA HUT RI',
        'WAKIL KETUA PANITIA HUT RI',
        'SEKRETARIS',
        'BENDAHARA',
    ]

    kepengurusan_inti = []

    for jabatan in jabatan_inti:
        anggota = Pengurus.objects.filter(
            jabatan__iexact=jabatan,
            divisi__isnull=True
        ).order_by('urutan')

        kepengurusan_inti.append({
            'jabatan': jabatan,
            'anggota': anggota,
        })

    divisi_list = Divisi.objects.order_by('urutan')
    kepengurusan_divisi = []

    for divisi in divisi_list:
        koordinator = Pengurus.objects.filter(
            divisi=divisi,
            is_koordinator=True
        ).order_by('urutan').first()

        anggota = Pengurus.objects.filter(
            divisi=divisi,
            is_koordinator=False
        ).order_by('urutan')

        kepengurusan_divisi.append({
            'nama': divisi.nama,
            'koordinator': koordinator,
            'anggota': anggota,
        })

    context = {
        'berita_terbaru': berita_terbaru,
        'agenda_terdekat': agenda_terdekat,
        'kepengurusan_inti': kepengurusan_inti,
        'kepengurusan_divisi': kepengurusan_divisi,
    }

    return render(request, 'core/home.html', context)