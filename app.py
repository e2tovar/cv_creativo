import os
import streamlit as st
from PIL import Image

from app.components.header import show_header
from app.components.social_links import show_social
from app.components.experience_and_skills import show_experience
from app.components.work_history import show_work_history
from app.components.education import show_education
from app.components.publications import show_publications
from app.components.soft_skill import show_soft_skills
from app.components.sidebar_bot import show_sidebar_bots
from app.components.footer import show_footer
from app.utils.text_utils import load_text_from_txt

from chatbot import Chatbot
from app.settings import PAGE_TITLE, PAGE_ICON, PROFILES_PIC_NAME, MAX_HISTORY, CV_TXT

# --- PATH ---
current_dir = os.path.dirname(os.path.abspath(__file__))
css_file = os.path.join(current_dir, "app", "styles", "main.css")
resume_file = os.path.join(current_dir, "app", "assets", "CV.pdf")
profile_pic = os.path.join(current_dir, "app", "assets", PROFILES_PIC_NAME)

cv_txt_path = os.path.join(current_dir, "app", "assets", CV_TXT)
cv_txt = load_text_from_txt(cv_txt_path)


# --- PAGE CONFIG ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF and PIC  ---
with open(css_file, "r", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_temp:
    PDFbyte = pdf_temp.read()
profile_pic = Image.open(profile_pic)

# --- INIT SESSION STATES ---
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = Chatbot()  # Inicializar el chatbot

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if 'show_disclaimer' not in st.session_state:
    st.session_state.show_disclaimer = True

# DEBUG
# st.write(f"History: {st.session_state.chat_history}")

# --- HEADER ---
show_header(profile_pic=profile_pic, cv_pdf=PDFbyte, download_name='EddyTovar.pdf')

# --- SOCIAL LINKS ---
show_social()

# --- EXPERIENCE ---
show_experience()

# --- WORK HISTORY ---
show_work_history()

# --- EDUCATION ---
show_education()

# --- PUBLICATIONS ---
show_publications()

# --- SOFT SKILLS ---
show_soft_skills()

# --- SIDEBAR BOT ---
chat_result = show_sidebar_bots(cv=cv_txt, botsito=st.session_state.chatbot)
# show_footer()
