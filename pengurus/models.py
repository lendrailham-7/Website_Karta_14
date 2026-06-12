from django.db import models

class Pengurus(models.Model):

    nama = models.CharField(max_length=100)

    jabatan = models.CharField(max_length=100)

    foto = models.ImageField(
        upload_to='pengurus/',
        blank=True,
        null=True
    )

    urutan = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):

        return f"{self.nama} - {self.jabatan}"