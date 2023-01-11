import openai
import streamlit as st
from gtts import gTTS 
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")


def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message.strip()

def speak(text):
    tts = gTTS(text=text, lang='es')
    tts.save("response.mp3")
    os.system("start response.mp3")

def chatbot():
    st.set_title("Chatbot")
    message = st.text_input("Enter your message:")
    if message:
        response = generate_text(message)
        st.success(response)
        speak(response)

if __name__ == "__main__":
    chatbot()
