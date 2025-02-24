import streamlit as st
from app.settings import NAME, DESCRIPTION

def show_header(profile_pic, cv_pdf, download_name):
    col1, col2 = st.columns(2, gap='small')
    with col1:
        st.image(profile_pic, width=230)

    # Divisor vertical con HTML
    st.markdown(
        """
        <style>
        .vertical-divider {
            border-left: 2px solid gray; !important
            height: 100%; !important
            margin: 0 10px; !important
        }
        </style>
        <div class="vertical-divider"></div>
        """,
        unsafe_allow_html=True
    )

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="Descargar CV",
            data=cv_pdf,
            file_name=download_name,
            mime="application/octet-stream",
        )
