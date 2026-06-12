from groq import Groq

from django.conf import settings


client = Groq(

    api_key=settings.GROQ_API_KEY_1

)


def ask_groq(messages):

    response = client.chat.completions.create(

        model='llama-3.3-70b-versatile',

        messages=messages,

        temperature=0.7

    )

    return response.choices[0].message.content