import openai_secret_manager
import openai
import streamlit as st
from gtts import gTTS 
import os

# Use the openai_secret_manager to get your API key
secrets = openai_secret_manager.get_secret("openai")
openai.api_key = secrets["api_key"]

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
