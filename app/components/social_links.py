import streamlit as st
from app.settings import SOCIAL_MEDIA

def show_social():
    cols = st.columns(len(SOCIAL_MEDIA))

    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        with cols[index]:
            cols[index].write(f'[{platform}]({link})')
