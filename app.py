import streamlit as st
from ollama import chat

MODEL = "qwen3.5:9b"

SYSTEM_PROMPT = """
You are a helpful AI assistant.
Answer directly in 1-3 sentences by default.
Do not display your thinking process.
Ask one short clarifying question when necessary.
"""

st.set_page_config(
    page_title="My Local AI",
    page_icon="🤖",
)

st.title("🤖 My Local AI")
st.caption("Powered by Ollama and Qwen")

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept a new question
if prompt := st.chat_input("Ask Qwen something..."):
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Generating response..."):
            try:
                response = chat(
                    model=MODEL,
                    messages=[
                        {
                            "role": "system",
                            "content": SYSTEM_PROMPT,
                        },
                        *st.session_state.messages,
                    ],
                    think=False,
                    options={
                        "temperature": 0.2,
                        "num_ctx": 4096,
                        "num_predict": 150,
                    },
                )

                answer = response.message.content
                st.markdown(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                    }
                )

            except Exception as error:
                st.error(f"Error communicating with Ollama: {error}")