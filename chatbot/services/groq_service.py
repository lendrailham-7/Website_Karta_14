from groq import Groq

from django.conf import settings


client_groq_1 = Groq(

    api_key=settings.GROQ_API_KEY_1

)


client_groq_2 = Groq(

    api_key=settings.GROQ_API_KEY_2

)


def ask_groq(messages):

    response = client_groq_1.chat.completions.create(

        model='llama-3.3-70b-versatile',

        messages=messages,

        temperature=0.7

    )

    return response.choices[0].message.content


def ask_groq_2(messages):

    response = client_groq_2.chat.completions.create(

        model='llama-3.3-70b-versatile',

        messages=messages,

        temperature=0.7

    )

    return response.choices[0].message.content