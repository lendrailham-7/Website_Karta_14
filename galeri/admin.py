from django.contrib import admin
from .models import Galeri

@admin.register(Galeri)
class GaleriAdmin(admin.ModelAdmin):

    list_display = (
        'judul',
        'tanggal'
    )

    search_fields = (
        'judul',
    )