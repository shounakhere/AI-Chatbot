# ✳ Minimal AI — LangChain Chatbot

A minimalist AI chatbot built using **LangChain, Ollama, and Streamlit**. It uses the locally running Llama 3.2 language model to generate responses without requiring an OpenAI API key.

The project features a clean, dark-themed chat interface and maintains conversation history so the AI can respond with context from previous messages.

## ✨ Features

- **Local AI Inference:** Uses Llama 3.2 through Ollama.
- **Minimalist UI:** Clean, dark-themed interface built with Streamlit.
- **Conversational Memory:** Maintains chat history throughout the current session.
- **Real-Time Interaction:** Ask questions and receive responses through a chat interface.
- **New Chat:** Clear the current conversation and start a new one.
- **Privacy-Friendly:** Prompts are processed by your local Ollama model rather than sent to a hosted LLM API.
- **No OpenAI API Key Required:** Run the chatbot locally without OpenAI API credits.

## 🛠️ Tech Stack

- **Python** — Core programming language.
- **LangChain** — Framework for interacting with language models.
- **Ollama** — Runs the Llama 3.2 model locally.
- **Streamlit** — Builds the chatbot user interface.

## 📁 Project Structure

```text
CHATBOT/
├── app.py              # Streamlit chatbot interface
├── chatbot2.py         # Command-line chatbot
├── requirements.txt    # Python dependencies
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
