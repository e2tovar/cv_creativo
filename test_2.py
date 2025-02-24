import streamlit as st


def on_input():
    st.session_state.input = 

st.write(f'El usuario ha escrito: ')

# Entrada del usuario
st.text_input("Escribe tu mensaje:", on_change=on_input)
