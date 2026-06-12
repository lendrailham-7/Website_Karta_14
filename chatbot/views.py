from django.shortcuts import render
from django.http import JsonResponse
import json
from .services.ai_router import ask_ai
from .services.knowledge_service import (
    get_pengurus_context
)
from .services.knowledge_service import (
    get_pengurus_context,
    get_agenda_context,
    get_berita_context,
    get_kontak_context,
)
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
        knowledge = (

    get_pengurus_context()

    +

    "\n"

    +

    get_agenda_context()
        
         +

    "\n"

    +

    get_berita_context()
     +

    "\n"

    +

    get_kontak_context()

)
        messages = [
        
            {
            
                'role': 'system',
        
                'content': f"""
        
        Kamu adalah chatbot resmi Karang Taruna.
        
        Gunakan data berikut
        untuk menjawab pertanyaan.
        
        {knowledge}
        
        Jika informasi tidak tersedia,
        sarankan pengguna untuk
        menghubungi pengurus.
        
        Jangan mengarang informasi.
        
        """
        
            }
        
        ] + history

        ai_reply = ask_ai(
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
