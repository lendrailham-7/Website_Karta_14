from django.db import models

class Berita(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    gambar = models.ImageField(
    upload_to='berita/',
    blank=True,
    null=True
)
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul