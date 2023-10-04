import streamlit as st
import random
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
time.clock = time.time
import collections.abc
collections.Hashable = collections.abc.Hashable

@st.cache_resource
def load_model():
    return ChatBot('xavier')

chatbot = load_model()

st.title("Xavier chatterbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = str(chatbot.get_response(prompt))
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})