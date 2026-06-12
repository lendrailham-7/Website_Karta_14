from django.shortcuts import render, get_object_or_404
from .models import Agenda

def daftar_agenda(request):
    agenda = Agenda.objects.all().order_by('tanggal')
    return render(request, 'agenda/daftar_agenda.html', {'agenda': agenda})

def detail_agenda(request, id):
    agenda = get_object_or_404(Agenda, id=id)
    return render(request, 'agenda/detail_agenda.html', {'agenda': agenda})