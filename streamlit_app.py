import openai
import streamlit as st
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

def chatbot():
    st.set_title("Chatbot")
    previous_message = None
    while True:
        message = st.text_input("Enter your message:", value=previous_message)
        if message:
            previous_message = message
            response = generate_text(message)
            st.success(response)
            if "exit" in message.lower():
                break

if __name__ == "__main__":
    chatbot()
