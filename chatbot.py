import os
from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st

from prompt import JOKER_PROMPT, WELCOME_PROMPT, CV_PROMPT

load_dotenv()

class Chatbot:
    def __init__(self):
        self.client = OpenAI(
            base_url=st.secrets["GITHUB_BASE"],
            api_key=st.secrets["GITHUB_KEY"],
        )

    def get_response(self, user_input, cv, chat_history):
        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": self.__generate_cv_prompt(cv, chat_history)},
                {"role": "user", "content": user_input}
            ],
            model="gpt-4o-mini",
            temperature=0.3
        )
        return response.choices[0].message.content

    def get_welcome(self):
        welcome_message = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": self.__generate_welcome_prompt()}
            ],
            model="gpt-4o-mini",
            temperature=0.85
        )

        return welcome_message.choices[0].message.content

    def get_question_joke(self, user_input):
        joke_message = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": self.__generate_joke_prompt(user_input)}
            ],
            model="gpt-4o-mini",
            temperature=0.8
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
