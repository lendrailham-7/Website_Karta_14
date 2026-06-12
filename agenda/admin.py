from django.contrib import admin
from .models import Agenda

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('nama_kegiatan', 'tanggal', 'waktu', 'lokasi')
    search_fields = ('nama_kegiatan', 'lokasi')
    list_filter = ('tanggal', 'lokasi')