import streamlit as st
from rag import ask_question

st.set_page_config(
    page_title="RAG Q&A Chatbot",
    page_icon="🤖",
)

st.title("🤖 RAG Q&A Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

question = st.chat_input("Ask a question...")

if question:

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    answer = ask_question(question)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])