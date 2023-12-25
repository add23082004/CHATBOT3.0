import streamlit as st
import openai
import speech_recognition as sr

openai.api_key = "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"


def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.write("Say something:")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        return user_input
    except sr.UnknownValueError:
        st.write("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        st.write(f"Speech recognition request failed: {e}")
        return ""


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


def main():
    st.title("Speech chatbot Chatbot")

    user_input_type = st.radio("Choose input type:", ["Text", "Speech"])

    if user_input_type == "Text":
        user_input = st.text_input("You:")
    else:
        user_input = speech_to_text()
        st.write("You (Speech):", user_input)

    if st.button("Chat"):
        response = chat_with_gpt(user_input)
        st.write("Chatbot:", response)


if __name__ == "__main__":
    main()
