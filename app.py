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

# --- Page Display Functions ---
def display_cv_page(profile_pic_img, cv_pdf_bytes):
    show_header(profile_pic=profile_pic_img, cv_pdf=cv_pdf_bytes, download_name='EddyTovar.pdf')
    show_social()
    show_experience()
    show_work_history()
    show_education()
    show_publications()
    show_soft_skills()

def display_chat_page(cv_text_content, chatbot_instance):
    st.title("Chat con EddyBot")
    chat_result = show_sidebar_bots(cv=cv_text_content, botsito=chatbot_instance)
    # We might need to handle/display chat_result here or within show_sidebar_bots

def display_thanks_page():
    st.title("¡Gracias!")
    st.markdown("Gracias por visitar esta página interactiva.")

def show_bottom_nav():
    nav_html = '''
    <div class="bottom-nav">
        <a href="?page=CV" target="_self">CV</a>
        <a href="?page=Chat" target="_self">Chat</a>
        <a href="?page=Thanks" target="_self">Agradecimientos</a>
    </div>
    '''
    st.markdown(nav_html, unsafe_allow_html=True)

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

if 'current_page' not in st.session_state:
    st.session_state.current_page = "CV"  # Default page

query_params = st.query_params
if "page" in query_params:
    page_param = query_params.get("page")[0]
    if page_param in ["CV", "Chat", "Thanks"]:
        st.session_state.current_page = page_param
        # Clear query params to avoid it sticking on refresh if not desired,
        # and to make sure subsequent clicks on the same nav item work as expected
        # after navigating away and back via other means (if any).
        st.query_params.clear()

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

# # --- HEADER ---
# show_header(profile_pic=profile_pic, cv_pdf=PDFbyte, download_name='EddyTovar.pdf')

# # --- SOCIAL LINKS ---
# show_social()

# # --- EXPERIENCE ---
# show_experience()

# # --- WORK HISTORY ---
# show_work_history()

# # --- EDUCATION ---
# show_education()

# # --- PUBLICATIONS ---
# show_publications()

# # --- SOFT SKILLS ---
# show_soft_skills()

# # --- SIDEBAR BOT ---
# chat_result = show_sidebar_bots(cv=cv_txt, botsito=st.session_state.chatbot)
# show_footer()

# --- Conditional Page Rendering ---
if st.session_state.current_page == "CV":
    # Ensure profile_pic (Image object) and PDFbyte (bytes) are available in this scope
    # These are loaded near the top of app.py
    display_cv_page(profile_pic_img=profile_pic, cv_pdf_bytes=PDFbyte)
elif st.session_state.current_page == "Chat":
    # Ensure cv_txt (string) and st.session_state.chatbot (Chatbot instance) are available
    # These are also initialized/loaded at the top or in session state
    display_chat_page(cv_text_content=cv_txt, chatbot_instance=st.session_state.chatbot)
elif st.session_state.current_page == "Thanks":
    display_thanks_page()
else: # Default or fallback
    st.error("Página no encontrada") # Or default to CV page
    display_cv_page(profile_pic_img=profile_pic, cv_pdf_bytes=PDFbyte)

show_bottom_nav()
