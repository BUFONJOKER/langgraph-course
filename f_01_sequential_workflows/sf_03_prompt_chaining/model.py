from langchain_ollama import ChatOllama

def load_model():   
    
    llm = ChatOllama(model='qwen3.5:cloud')

    return llm