import streamlit as st
import random

quotes = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "The only way to do great work is to love what you do.",
    "Don't watch the clock; do what it does. Keep going.",
    "It does not matter how slowly you go as long as you do not stop.",
    "You are never too old to set another goal or to dream a new dream.",
]


def main():
    st.set_page_config(page_title="Growth Mindset Challenge")
    st.title("Growth Mindset Challenge no 1")
    st.write("Believe in your ability to grow and improve!")

    st.subheader("✨ Today's Motivational quote:")
    st.write(random.choice(quotes))
    # User Quiz
    st.subheader("🧠 Growth Mindset Quiz")
    st.write("Test yourself and see how much you embrace a growth mindset!")

    question = "When you face a challenge, what do you do?"

    options = [
        "Give up",
        "Try again and learn from mistakes",
        "Blame others",
        "Ignore it",
    ]
    answer = st.radio(question, options)

    if st.button("Submit Answer"):
        if answer == "Try again and learn from mistakes":
            st.success("🎉 Correct! This is the essence of a growth mindset!")
        else:
            st.error(
                "❌ Not quite! A growth mindset means learning and improving from challenges."
            )

    # User Reflection
    st.subheader("💭 Reflect on Your Journey")
    user_input = st.text_area("Write about a time you overcame a challenge:")
    if st.button("Submit Reflection"):
        if len(user_input) < 10:
            st.error("Please provide a more detailed reflection.")
        else:
            st.success("Great! Reflection helps reinforce a growth mindset.")

    st.write("---")
    st.write("Developed by Abdul Samad 🚀")


if __name__ == "__main__":
    main()
