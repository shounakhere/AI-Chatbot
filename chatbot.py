
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama

model = ChatOllama(model="llama3.2")

chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    chat_history.append(HumanMessage(content=user_input))

    result = model.invoke(chat_history)

    print("AI:", result.content)

    chat_history.append(AIMessage(content=result.content))
