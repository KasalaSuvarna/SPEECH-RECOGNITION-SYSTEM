

import speech_recognition as sr
import tkinter as tk
from tkinter import messagebox

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        output_label.config(text="🎙️ Listening...")
        root.update()

        try:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5)
            output_label.config(text="🧠 Recognizing...")
            root.update()
            text = recognizer.recognize_google(audio)
            output_label.config(text="✅ You said:\n" + text)
        except sr.WaitTimeoutError:
            output_label.config(text="⏱️ No speech detected. Try again.")
        except sr.UnknownValueError:
            output_label.config(text="❌ Could not understand audio.")
        except sr.RequestError:
            output_label.config(text="❌ API unavailable. Check internet connection.")

# GUI setup
root = tk.Tk()
root.title("🎤 Speech Recognition System")
root.geometry("450x300")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

# Title label
title_label = tk.Label(
    root,
    text="Speech Recognition",
    font=("Arial", 20, "bold"),
    bg="#f2f2f2",
    fg="#333"
)
title_label.pack(pady=20)

# Output label
output_label = tk.Label(
    root,
    text="Click 'Start Listening' to begin.",
    wraplength=400,
    font=("Arial", 13),
    bg="#f2f2f2",
    fg="#555",
    justify="center"
)
output_label.pack(pady=30)

# Listen button
listen_button = tk.Button(
    root,
    text="🎙️ Start Listening",
    font=("Arial", 14),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5,
    command=recognize_speech
)
listen_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
