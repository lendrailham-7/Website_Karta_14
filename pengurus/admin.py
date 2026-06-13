from django.contrib import admin

from .models import Divisi, Pengurus


@admin.register(Divisi)
class DivisiAdmin(admin.ModelAdmin):

    list_display = (
        'nama',
        'urutan',
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
        'urutan',
        'is_koordinator',
    )

    list_filter = (
        'divisi',
        'is_koordinator',
    )

    list_editable = (
        'urutan',
        'is_koordinator',
    )

    search_fields = (
        'nama',
        'jabatan',
    )

    ordering = (
        'urutan',
    )