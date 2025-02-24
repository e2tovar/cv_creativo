import streamlit as st
import time

from chatbot import Chatbot
from app.utils.embeddings_utils import find_most_relevant_chunk, get_all_cv
from app.utils.images import image_to_base64


def show_sidebar_bots(chunks, embeddings, model_embeddigns, botsito):
    with st.sidebar:
        st.text_input(
            'pregunta',
            label_visibility="hidden",
            key="user_input",
            on_change=__call_chatbot,
            args=(botsito, chunks, embeddings, model_embeddigns)
            )

        __show_sidebar_welcome_bot(botsito, st.session_state.chat_history)

        if st.session_state.chat_history:
            st.markdown("---")
            rsp = st.session_state.chat_history[-1][1]
            __efecto_escritura(rsp)

def __show_sidebar_welcome_bot(botsito: Chatbot, chat_history=[]):
    # Read if there is a label on the sidebar input
    with st.sidebar:
        if not chat_history:
            welcome_msg = botsito.get_welcome()
            texto = welcome_msg
        else:
            joke = botsito.get_question_joke(user_input=chat_history[-1][0])
            texto = joke
        # Add bot gif with markdown
        gif_path = "app/assets/bot3.gif"
        image_base64 = image_to_base64(gif_path)

        st.markdown(
            f"""
            <div class="container">
            <img src="data:image/jpeg;base64,{image_base64}" alt="Image" class="top-right-image">
            <p>
                {texto}
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )


def __call_chatbot(botsito: Chatbot, chunks, embeddings, model_embeddings):
    user_input = st.session_state.user_input
    if user_input:
        relevant_chunk = find_most_relevant_chunk(user_input, chunks, embeddings, model_embeddings)
        relevant_chunk = get_all_cv()
        response = botsito.get_response(user_input, relevant_chunk)
        st.session_state.chat_history.append((user_input + '-----' + relevant_chunk, response))


# Función para simular el efecto de escritura
def __efecto_escritura(texto, delay=0.02):
    placeholder = st.empty()  # Crea un espacio vacío para el texto
    texto_parcial = ""
    for caracter in texto:
        texto_parcial += caracter  # Agrega un caracter a la vez
        placeholder.markdown(f"**{texto_parcial}**")  # Muestra el texto parcial
        time.sleep(delay)  # Retraso entre caracteres
