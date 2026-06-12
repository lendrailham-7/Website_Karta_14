from django.db import models


class Divisi(models.Model):

    nama = models.CharField(max_length=100)

    urutan = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nama


class Pengurus(models.Model):

    nama = models.CharField(max_length=100)

    jabatan = models.CharField(max_length=100)

    divisi = models.ForeignKey(
        Divisi,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    foto = models.ImageField(
        upload_to='pengurus/',
        blank=True,
        null=True
    )

    deskripsi = models.TextField(
        blank=True,
        null=True
    )

    urutan = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return self.nama