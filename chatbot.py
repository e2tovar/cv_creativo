from groq import Groq
from dotenv import load_dotenv
import streamlit as st

from prompt import JOKER_PROMPT, WELCOME_PROMPT, CV_PROMPT
from app.settings import MODEL_CHATBOT

load_dotenv()

class Chatbot:
    def __init__(self):
        self.client = Groq(
            api_key=st.secrets["API_KEY"],
        )

    def get_response(self, user_input, cv, chat_history):
        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": self.__generate_cv_prompt(cv, chat_history)},
                {"role": "user", "content": user_input}
            ],
            model=MODEL_CHATBOT,
            temperature=0.2,
            reasoning_format="hidden"
        )
        return response.choices[0].message.content

    def get_welcome(self):
        try:
            welcome_message = self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": self.__generate_welcome_prompt()}
                ],
                model=MODEL_CHATBOT,
                temperature=0.85,
                reasoning_format="hidden"
            )

            return welcome_message.choices[0].message.content
        except Exception as e:
            # Devuelve el mensaje
            msg = "Lo siento, Eddy no quiere pagar más por mí, hemos alcanzado el límite de peticiones. Prueba en un rato..."
            return f"{msg}"

    def get_question_joke(self, user_input):
        joke_message = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": self.__generate_joke_prompt(user_input)}
            ],
            model=MODEL_CHATBOT,
            temperature=0.8,
            reasoning_format="hidden"
        )

        return joke_message.choices[0].message.content

    @staticmethod
    def __generate_welcome_prompt():
        return WELCOME_PROMPT

    @staticmethod
    def __generate_joke_prompt(user_input):
        return JOKER_PROMPT.format(user_input)

    @staticmethod
    def __generate_cv_prompt(context, chat_history):
        return CV_PROMPT.format(context, chat_history)
