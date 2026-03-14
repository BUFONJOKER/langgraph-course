from langchain_ollama import ChatOllama

def load_model():
    '''this function loads the model qwen3.5:cloud using ollama'''
    return ChatOllama(model="qwen3.5:cloud")