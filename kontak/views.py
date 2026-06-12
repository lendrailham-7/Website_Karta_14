from django.shortcuts import render

def kontak(request):

    context = {

        'alamat': 'Jl. Contoh No. 14',

        'whatsapp': '628123456789',

        'email': 'karangtaruna@gmail.com',

        'instagram': '@karangtaruna_rw14',

        'jam': 'Senin - Jumat, 08.00 - 17.00'

    }

    return render(

        request,

        'kontak/kontak.html',

        context

    )