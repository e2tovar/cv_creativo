import streamlit as st
import time

from chatbot import Chatbot
from app.utils.images import image_to_base64


def show_sidebar_bots(botsito, cv):
    with st.sidebar:
        if st.session_state.show_disclaimer:
            st.markdown(
                """
                <div class="container">
                    <p>
                        <b>NOTA:</b> Este chatbot es una BETA. Proporciona información sobre el CV de Eddy Tovar,
                        pero no es un asistente profesional. Puede contener errores. Para consultas directas, contacta a Eddy.
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.session_state.show_disclaimer = False
            st.button("Entendido")

        else:
            st.text_input(
                'pregunta',
                label_visibility="hidden",
                key="user_input",
                on_change=__call_chatbot,
                args=(botsito, cv, st.session_state.chat_history)
                )

            __show_sidebar_welcome_bot(botsito, st.session_state.chat_history)

            if st.session_state.chat_history:
                st.markdown("---")
                st.write("Aquí tu respuesta: ")
                rsp = st.session_state.chat_history[-1][1]
                __efecto_escritura(rsp)

def __show_sidebar_welcome_bot(botsito: Chatbot, chat_history=[]):
    # Read if there is a label on the sidebar input
    with st.sidebar:
        if not chat_history:
            welcome_msg = botsito.get_welcome()
            texto = welcome_msg
        else:
            print(chat_history[-1][0])
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


def __call_chatbot(botsito: Chatbot, cv, chat_history):
    user_input = st.session_state.user_input
    if user_input:
        response = botsito.get_response(user_input, cv, chat_history)
        st.session_state.chat_history.append((user_input, response))


# Función para simular el efecto de escritura
def __efecto_escritura(texto, delay=0.02):
    placeholder = st.empty()  # Crea un espacio vacío para el texto
    texto_parcial = ""
    for caracter in texto:
        texto_parcial += caracter  # Agrega un caracter a la vez
        placeholder.markdown(f"**{texto_parcial}**")  # Muestra el texto parcial
        time.sleep(delay)  # Retraso entre caracteres
