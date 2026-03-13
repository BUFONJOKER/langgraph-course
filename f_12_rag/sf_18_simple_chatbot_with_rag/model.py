from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

def load_model():
    '''Load the Ollama model for RAG.'''

    model = ChatOllama(model="qwen3.5:cloud")

    return model

def load_embeddings_model():
    '''Load huggingface sentence transformer model for RAG.'''

    embeddings = HuggingFaceEndpointEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
    return embeddings