from django.contrib import admin

from .models import Divisi, Pengurus


@admin.register(Divisi)
class DivisiAdmin(admin.ModelAdmin):

    list_display = (
        'nama',
        'urutan'
    )

    list_editable = (
        'urutan',
    )

    ordering = (
        'urutan',
    )


@admin.register(Pengurus)
class PengurusAdmin(admin.ModelAdmin):

    list_display = (
        'nama',
        'jabatan',
        'divisi',
        'urutan'
    )

    list_filter = (
        'divisi',
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