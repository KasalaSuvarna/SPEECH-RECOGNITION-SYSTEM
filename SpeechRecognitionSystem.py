import streamlit as st
import speech_recognition as sr

st.title("🎤 Speech Recognition System")
st.write("Click the button below to record your voice and convert it to text.")

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to recognize speech
def recognize_speech_from_mic():
    with sr.Microphone() as source:
        st.info("Adjusting for background noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source)
        st.info("Listening... Speak now.")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        try:
            st.info("Recognizing...")
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError:
            return "Could not request results from Google Speech Recognition service."

# Record button
if st.button("🎙️ Start Recording"):
    result = recognize_speech_from_mic()
    st.subheader("📝 Transcribed Text:")
    st.success(result)
