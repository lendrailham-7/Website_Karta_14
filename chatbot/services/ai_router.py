from .groq_service import (
    ask_groq,
    ask_groq_2
)

from .gemini_service import (
    ask_gemini
)

SYSTEM_PROMPT = """
Kamu adalah chatbot resmi Karang Taruna.

Aturan menjawab:

1. Jawab dengan sopan, jelas, dan ringkas.
2. Gunakan informasi dari knowledge base jika tersedia.
3. Jika informasi tidak tersedia, katakan dengan jujur bahwa data belum tersedia.
4. Jika memberikan daftar, langkah-langkah, atau beberapa poin, tampilkan setiap poin pada baris baru.
5. Jangan menggabungkan beberapa poin dalam satu paragraf.
6. Jika jawaban berupa penjelasan umum, gunakan paragraf yang rapi dan mudah dibaca.
7. Jangan mengarang informasi.
8. Jika ditanya tentang kepengurusan jawab dari pengurus sampai semua divisi dan jangan menyebut pengurus inti, jawab saja semua pengurus
"""

def ask_ai(messages):

    messages = [

        {

            "role": "system",

            "content": SYSTEM_PROMPT

        }

    ] + messages

    try:

        return ask_groq(messages)

    except Exception as e:

        print(

            "Groq 1 gagal:",

            e

        )

        try:

            return ask_groq_2(messages)

        except Exception as e:

            print(

                "Groq 2 gagal:",

                e

            )

            try:

                return ask_gemini(messages)

            except Exception as e:

                print(

                    "Gemini gagal:",

                    e

                )

                return (

                    "Maaf, layanan chatbot "

                    "sedang mengalami gangguan. "

                    "Silakan coba beberapa saat lagi."

                )