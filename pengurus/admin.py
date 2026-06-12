from django.contrib import admin
from .models import Pengurus

@admin.register(Pengurus)
class PengurusAdmin(admin.ModelAdmin):

    list_display = (
        'nama',
        'jabatan',
        'urutan'
    )

    list_editable = (
        'urutan',
    )

    search_fields = (
        'nama',
        'jabatan'
    )

    ordering = (
        'urutan',
    )