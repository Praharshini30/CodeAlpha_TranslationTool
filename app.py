import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Language Translation Tool")

text = st.text_area("Enter text")

languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-CN"
}

source = st.selectbox("Source Language", list(languages.keys()))
target = st.selectbox("Target Language", list(languages.keys()))

if st.button("Translate"):

    if source == target:
        st.warning("Choose different languages.")

    elif text.strip():

        translated = GoogleTranslator(
            source=languages[source],
            target=languages[target]
        ).translate(text)

        st.success("Translation completed!")
        st.write("Translated Text:")
        st.code(translated)

    else:
        st.warning("Please enter some text first.")