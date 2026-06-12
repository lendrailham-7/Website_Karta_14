from .groq_service import ask_groq
from .gemini_service import ask_gemini


def ask_ai(messages):

    try:

        return ask_groq(messages)

    except Exception as e:

        print("Groq 1 gagal:", e)

        try:

            return ask_groq_2(messages)

        except Exception as e:

            print("Groq 2 gagal:", e)

            return ask_gemini(messages)