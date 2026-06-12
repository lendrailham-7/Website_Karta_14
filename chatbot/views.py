from django.shortcuts import render
from django.http import JsonResponse
import json


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

        history = history[-10:]

        request.session['chat_history'] = history

        return JsonResponse({

            'reply': 'Halo! AI sedang dalam tahap pengembangan.',

            'history_count': len(history)

        })

    return JsonResponse({

        'error': 'Method tidak diizinkan.'

    })