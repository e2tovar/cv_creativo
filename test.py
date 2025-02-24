import streamlit as st

# Inicializar el historial de la conversación
if 'history' not in st.session_state:
    st.session_state['history'] = []

# Función para agregar mensajes al historial
def add_to_history(role, message):
    st.session_state['history'].append({"role": role, "message": message})

# Callback para manejar la entrada del usuario
def on_input_change():
    user_input = st.session_state.user_input
    if user_input:
        # Agregar el mensaje del usuario al historial
        add_to_history("Usuario", user_input)

        # Lógica del bot (en este caso, simplemente repite el mensaje)
        bot_response = f"Escuché que dijiste '{user_input}'"

        # Agregar la respuesta del bot al historial
        add_to_history("Bot", bot_response)

        # Limpiar la entrada del usuario
        st.session_state.user_input = ""

# Interfaz de usuario
st.title("Chatbot Simple con Callback")


# Entrada del usuario con callback
st.text_input(
    "Escribe tu mensaje:",
    key="user_input",
    on_change=on_input_change
)

# Mostrar el historial de la conversación
for chat in st.session_state['history']:
    st.write(f"{chat['role']}: {chat['message']}")