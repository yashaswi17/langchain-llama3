from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama.llms import OllamaLLM 
import streamlit as st 
import os

'''Prompt Template'''

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system"
            "you are an expert in data science "
            "and a helpful assitant."
        ),
        ("user", "Question : {question}"),
    ]
)
"Streamlit Framework"

st.title("langchain project")
input_text =  st.text_input("search the topic you want ")

"ollama"

llm = OllamaLLM (model = "llama3.2:1b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question" : input_text}))