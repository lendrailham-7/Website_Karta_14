from django.db import models

class Agenda(models.Model):
    nama_kegiatan = models.CharField(max_length=200)
    deskripsi = models.TextField()
    lokasi = models.CharField(max_length=200)
    tanggal = models.DateField()
    waktu = models.TimeField()
    gambar = models.ImageField(upload_to='agenda/', blank=True, null=True)

    def __str__(self):
        return self.nama_kegiatan