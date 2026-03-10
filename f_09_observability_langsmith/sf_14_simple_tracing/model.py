from langchain_ollama import ChatOllama
import streamlit as st

@st.cache_resource
def load_model():
  '''
  This function load qwen3.5:cloud ollama model.
  '''

  model = ChatOllama(model='qwen3.5:cloud')

  return model