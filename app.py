import streamlit as st
from langchain_ollama import ChatOllama

# Page configuration
st.set_page_config(
    page_title="AI CHATBOT",
    page_icon="✳",
    layout="centered"
)

# Minimalist styling
st.markdown("""
<style>
    .stApp {
        background-color: #0f1117;
        color: #f5f5f5;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        max-width: 800px;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    h1 {
        font-size: 2rem;
        font-weight: 650;
        letter-spacing: -1px;
    }

    .subtitle {
        color: #9296a3;
        font-size: 14px;
        margin-top: -12px;
        margin-bottom: 30px;
    }

    [data-testid="stChatMessage"] {
        border: 1px solid #292c35;
        border-radius: 16px;
        padding: 16px;
        margin-bottom: 12px;
    }

    [data-testid="stChatInput"] {
        border-color: #343741;
    }

    .stButton button {
        border-radius: 10px;
        border: 1px solid #343741;
    }

    .status {
        display: inline-block;
        color: #a5e6b0;
        font-size: 12px;
        border: 1px solid #294a32;
        background: #17251b;
        padding: 5px 10px;
        border-radius: 20px;
        margin-bottom: 18px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize model
@st.cache_resource
def load_model():
    return ChatOllama(
        model="llama3.2",
        temperature=0.7
    )

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hey! I'm your AI assistant. What would you like to explore today?"
        }
    ]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Header
st.markdown('<div class="status">● LOCAL MODEL · LLAMA 3.2</div>',
            unsafe_allow_html=True)

st.title("AI CHATBOT")
st.markdown(
    '<p class="subtitle">A quiet space to think, ask, and explore.</p>',
    unsafe_allow_html=True
)

# Clear chat button
left, right = st.columns([5, 1])

with right:
    if st.button("＋ New chat", use_container_width=True):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hey! I'm your AI assistant. What would you like to explore today?"
            }
        ]
        st.session_state.chat_history = []
        st.rerun()

# Display existing messages
for message in st.session_state.messages:
    avatar = "🧑" if message["role"] == "user" else "✳"

    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Input at the bottom
if prompt := st.chat_input("Message Minimal AI..."):

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    # Add user input to LangChain history
    st.session_state.chat_history.append({
        "role": "human",
        "content": prompt
    })

    try:
        model = load_model()

        from langchain_core.messages import (
            SystemMessage,
            HumanMessage,
            AIMessage
        )

        # Reconstruct LangChain messages
        history = [
            SystemMessage(
                content="You are a helpful assistant. Be clear and concise."
            )
        ]

        for message in st.session_state.chat_history:
            if message["role"] == "human":
                history.append(
                    HumanMessage(content=message["content"])
                )
            else:
                history.append(
                    AIMessage(content=message["content"])
                )

        # Generate response
        with st.chat_message("assistant", avatar="✳"):
            with st.spinner("Thinking..."):
                result = model.invoke(history)
                response = result.content

            st.markdown(response)

        # Save AI response
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        st.session_state.chat_history.append({
            "role": "ai",
            "content": response
        })

    except Exception as e:
        error_message = (
            "I couldn't connect to Ollama. Make sure Ollama is running "
            "and that the llama3.2 model is installed."
        )

        st.error(error_message)

        # Remove the unanswered user turn from model history
        if (
            st.session_state.chat_history
            and st.session_state.chat_history[-1]["role"] == "human"
        ):
            st.session_state.chat_history.pop()

        # Remove the failed user message from displayed history
        if (
            st.session_state.messages
            and st.session_state.messages[-1]["role"] == "user"
        ):
            st.session_state.messages.pop()

        st.caption(f"Technical details: {e}")
        st.rerun()
