import streamlit as st
from auth import auth_page
from main_app import main_app

if __name__ == "__main__":
    if "username" not in st.session_state:
        auth_page()
    else:
        main_app()
