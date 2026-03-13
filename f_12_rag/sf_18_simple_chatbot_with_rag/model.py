from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

def load_model(model_name: str):
    '''Load the given model from ollama for RAG.'''

    model = ChatOllama(model=model_name)

    return model

def load_embeddings_model(model_name: str):
    '''Load given embedding model from huggingface for RAG.'''

    embeddings = HuggingFaceEndpointEmbeddings(model=model_name)
    return embeddings