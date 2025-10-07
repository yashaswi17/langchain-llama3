import streamlit as st
from langchain_ollama import OllamaLLM

"initialize"

llm = OllamaLLM (model = "llama3.2:1b")

st.title("llama3 chat-bot")

"chat history initialize"
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role" : "assitant", "content" :
          "how can I help you?"
        }
    ]
"message history"
for msg in st.session_state.messages :
    st.chat_message(
        msg["role"], avatar="🥷" if msg["role"] == "user" else "🤖"
    ).write(msg["content"])

"generate response"
def generate_response():
    messages = [
        {"role" : msg ["role"], "content": msg["content"]}
        for msg in st.session_state.messages
    ]
#last user msg

    prompt = messages[-1]["content"]

    response = llm.stream(input=prompt)
    full_response = ""
    for token in response :
        full_response += token
        yield token
    st.session_state ["full_response"] = full_response

"user input"
if prompt := st.chat_input():
    st.session_state.messages.append({"role" : "user" , "content" : prompt})
    st.chat_message("user", avatar= "🥷").write(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        response = st.write_stream(generate_response())

    st.session_state.messages.append(
        {"role" : "assistant", "content": st.session_state["full_response"]
        }
    )    