import google.generativeai as genai

from django.conf import settings


genai.configure(

    api_key=settings.GEMINI_API_KEY

)


model = genai.GenerativeModel(

    'gemini-2.5-flash'

)


def ask_gemini(messages):

    prompt = ""

    for msg in messages:

        role = msg.get(

            'role',

            ''

        )

        content = msg.get(

            'content',

            ''

        )

        prompt += f"{role}: {content}\n"

    response = model.generate_content(

        prompt

    )

    return response.text