import streamlit as st
from Flashcard import main  # Assuming your main logic is in Flashcard.py

st.title("Anki Flashcard Generator")

# File uploader
uploaded_file = st.file_uploader("Upload podcast script", type="txt")

if uploaded_file is not None:
    # Read the file content
    script_content = uploaded_file.read().decode("utf-8")

    # Topic input
    topic = st.text_input("Enter the main topic")

    # Generate button
    if st.button("Generate Flashcards"):
        # Call your main function
        main(script_content, topic)

        # Provide download link
        with open("anki_flashcards.csv", "rb") as f:
            st.download_button("Download CSV", f, file_name="anki_flashcards.csv")