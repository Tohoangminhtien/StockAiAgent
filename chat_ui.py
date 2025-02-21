import streamlit as st
import os
from dotenv import load_dotenv
from agent import ChatAgent

# Load environment variables
load_dotenv('private/.env')
OPENAI_API_KEY = os.getenv("OPEN_AI_KEY")
chat = ChatAgent(OPENAI_API_KEY)

st.title("AI Stock Chatbot")

# Hiển thị ảnh trong sidebar nếu có
image_folder = "chart"
if os.path.exists(image_folder):
    image_files = [f for f in os.listdir(image_folder) if f.endswith(
        (".png", ".jpg", ".jpeg", ".gif"))]

    if image_files:
        st.sidebar.header("📊 Saved Charts")
        for img_file in image_files:
            img_path = os.path.join(image_folder, img_file)
            st.sidebar.image(img_path, caption=img_file,
                             use_container_width=True)

# Khởi tạo session state cho tin nhắn
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
