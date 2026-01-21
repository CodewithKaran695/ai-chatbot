from django.shortcuts import render
from groq import Groq
import os
# Create your views here.

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat_page(request):
    user_message = None
    ai_reply = None

    if request.method == 'POST':
        user_message = request.POST.get("message")

        if user_message:
            response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {
            "role": "system",
            "content": (
                "You are a helpful and friendly AI assistant. "
                "Structure answers clearly using headings and subheadings. "
                "Headings should be short and meaningful. "
                "Use emojis where appropriate. "
                "Break content into short paragraphs or bullet points."
            )
        },
        {
            "role": "user",
            "content": user_message
        }
    ]
)

            

            ai_reply = response.choices[0].message.content

    return render(request, "chatbot/chat.html", {
        "user_message": user_message,
        "ai_reply": ai_reply
    })