import streamlit as st
from data import load_users, save_users


def login():
    st.subheader("Login")
    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login"):
        users = load_users()
        if username in users and users[username] == password:
            st.session_state.username = username
            st.success(f"Logged in as {username}")
            st.rerun()  # Refresh to load the main app
        else:
            st.error("Invalid username or password")


def signup():
    required_number = "1234567890"
    required_symbol = "!@#$%^&*_-"

    st.subheader("Create Account")
    new_username = st.text_input("Choose a Username", key="signup_username")
    if new_username:
        if len(new_username) < 6 or len(new_username) > 30:
            st.error("The username length should be between 6 and 30 characters")
    new_password = st.text_input(
        "Choose a Password", type="password", key="signup_password"
    )
    confirm_password = st.text_input(
        "Confirm Password", type="password", key="signup_confirm"
    )

    if st.button("Sign Up"):
        if len(new_password) < 8:
            st.error("The password should be at least 8 characters long")
        elif not (
            any(symb in required_symbol for symb in new_password)
            and any(num in required_number for num in new_password)
        ):
            st.error(
                "The password should contain at least one special character and one number"
            )
        elif new_password != confirm_password:
            st.error("Passwords do not match!")
        else:
            users = load_users()
            if new_username in users:
                st.error("Username already exists! Please choose another.")
            else:
                users[new_username] = new_password
                save_users(users)
                st.success("Account created successfully! Please log in.")


def auth_page():
    st.title("Welcome to the Growth Challenge Tracker")
    auth_mode = st.radio("Select Option", ("Login", "Sign Up"))
    if auth_mode == "Login":
        login()
    else:
        signup()
