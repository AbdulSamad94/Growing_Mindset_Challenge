import streamlit as st
from datetime import datetime
from data import load_data, save_data
from challenges import get_daily_challenge, get_motivational_quote


def main_app():
    st.set_page_config(page_title="Daily Growth Challenge Tracker", page_icon="")
    st.title("🌱 Daily Growth Challenge Tracker")
    st.write("Embrace a daily challenge to build a growth mindset!")

    # Initialize challenge and quote only once
    if "challenge" not in st.session_state:
        st.session_state.challenge = get_daily_challenge()
    if "quote" not in st.session_state:
        st.session_state.quote = get_motivational_quote()

    st.subheader("Today's Challenge")
    st.info(st.session_state.challenge)

    st.subheader("Motivational Quote")
    st.write(f'"{st.session_state.quote}"')

    # Reflection Form
    st.subheader("Challenge Impact on you")
    completed = st.checkbox("I have completed today's challenge")
    reflection = st.text_area(
        "What was the impact of the challenge on your experience today:",
        height=150,
        key="reflection_input",
    )

    if st.button("Submit the impact"):
        if not reflection.strip():
            st.error("Please share valid description!")
        else:
            data = load_data()
            new_entry = {
                "username": st.session_state.username,
                "date": datetime.now().strftime("%Y-%m-%d"),
                "challenge": st.session_state.challenge,
                "completed": completed,
                "reflection": reflection.strip(),
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            data["entries"].append(new_entry)
            save_data(data)
            st.success("Your reflection has been saved!")

    st.write("---")
    st.subheader("Your Past Reflections")
    data = load_data()
    user_entries = [
        entry
        for entry in data["entries"]
        if entry.get("username") == st.session_state.username
    ]
    if user_entries:
        for entry in reversed(user_entries):
            st.markdown(
                f"**Date:** {entry['date']} - **Challenge:** {entry['challenge']}"
            )
            st.markdown(f"**Completed:** {'Yes' if entry['completed'] else 'No'}")
            st.markdown(f"**Reflection:** {entry['reflection']}")
            st.markdown(f"**Timestamp:** {entry['timestamp']}")
            st.write("---")
    else:
        st.info("No past reflections yet. Start your journey today!")
