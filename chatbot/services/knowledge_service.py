from pengurus.models import Pengurus
from agenda.models import Agenda
from berita.models import Berita


def get_pengurus_context():

    pengurus = Pengurus.objects.select_related(
        'divisi'
    ).order_by(
        'urutan'
    )

    context = "DATA PENGURUS KARANG TARUNA:\n\n"

    for p in pengurus:

        divisi = (
            p.divisi.nama
            if p.divisi
            else "Pengurus Inti"
        )

        context += (

            f"Nama: {p.nama}\n"

            f"Jabatan: {p.jabatan}\n"

            f"Divisi: {divisi}\n\n"

        )

    return context
def get_agenda_context():

    agenda = Agenda.objects.order_by(
        'tanggal'
    )[:5]

    context = "DATA AGENDA KARANG TARUNA:\n\n"

    for a in agenda:

        context += (

            f"Nama Agenda: {a.nama_kegiatan}\n"

            f"Tanggal: {a.tanggal}\n"

            f"Deskripsi: {a.deskripsi}\n\n"

        )

    return context

def get_berita_context():

    berita = Berita.objects.order_by(
        '-tanggal'
    )[:5]

    context = "DATA BERITA KARANG TARUNA:\n\n"

    for b in berita:

        context += (

            f"Judul: {b.judul}\n"

            f"Isi: {b.isi[:200]}\n\n"

        )

    return context