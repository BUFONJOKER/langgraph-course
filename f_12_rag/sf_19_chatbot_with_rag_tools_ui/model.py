from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

@st.cache_resource
def load_model(model_name: str):
    '''Load the given model from ollama for RAG.'''

    model = ChatOllama(model=model_name)

    return model

@st.cache_resource
def load_embeddings_model(model_name: str):
    '''Load given embedding model from huggingface for RAG.'''

    embeddings = HuggingFaceEndpointEmbeddings(model=model_name)
    return embeddings