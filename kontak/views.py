from django.shortcuts import render

def kontak(request):

    context = {

        'alamat': 'Jl. Sariwates, Antapani Kidul',

        'whatsapp': '628123456789',

        'email': 'xxxxxx@gmail.com',

        'instagram': '@kartasariwates14',

        'jam': 'Senin - Jumat, 08.00 - 17.00'

    }

    return render(

        request,

        'kontak/kontak.html',

        context

    )