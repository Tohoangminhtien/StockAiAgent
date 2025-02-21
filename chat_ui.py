import streamlit as st
import os
from dotenv import load_dotenv
from agent import ChatAgent

load_dotenv('private/.env')
OPENAI_API_KEY = os.getenv("OPEN_AI_KEY")
chat = ChatAgent(OPENAI_API_KEY)

st.title("AI Stock Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Say something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.spinner("Thinking..."):
        reply = chat.chat(st.session_state.messages)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
