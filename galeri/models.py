from django.db import models

class Galeri(models.Model):

    judul = models.CharField(max_length=200)

    deskripsi = models.TextField(blank=True)

    gambar = models.ImageField(
        upload_to='galeri/'
    )

    tanggal = models.DateField(
        auto_now_add=True
    )

    def __str__(self):

        return self.judul