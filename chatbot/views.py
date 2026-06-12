from django.shortcuts import render
from django.http import JsonResponse
import json
from .services.groq_service import ask_groq

def chat_page(request):

    return render(

        request,

        'chatbot/chatbot.html'

    )

def send_message(request):

    if request.method == 'POST':

        data = json.loads(
            request.body
        )

        user_message = data.get(
            'message',
            ''
        )

        history = request.session.get(
            'chat_history',
            []
        )

        history.append({

            'role': 'user',

            'content': user_message

        })

        messages = [

            {

                'role': 'system',

                'content': '''
                Kamu adalah chatbot resmi Karang Taruna.

                Jawablah pertanyaan dengan sopan,
                singkat, dan mudah dipahami.

                Jika tidak mengetahui jawaban,
                sarankan pengguna menghubungi
                pengurus melalui halaman kontak.

                Jangan mengarang informasi.
                '''

            }

        ] + history

        ai_reply = ask_groq(
            messages
        )

        history.append({

            'role': 'assistant',

            'content': ai_reply

        })

        history = history[-10:]

        request.session[
            'chat_history'
        ] = history

        return JsonResponse({

            'reply': ai_reply

        })

    return JsonResponse({

        'error': 'Method tidak diizinkan.'

    })