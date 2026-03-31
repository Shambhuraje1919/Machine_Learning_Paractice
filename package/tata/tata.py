import streamlit as st
from groq import Groq

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot powered by Groq")

client = Groq(api_key="REMOVED_SECRET")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
with st.spinner("Thinking..."):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant named Jarvis. You were created by Shambhu. You are not Meta AI or any other AI. Never mention Llama or Meta. Always say you are Jarvis."
            }
        ] + st.session_state.messages
    )
    reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()