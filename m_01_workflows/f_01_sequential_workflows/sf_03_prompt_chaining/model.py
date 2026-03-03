from langchain_ollama import ChatOllama

def load_model():   
    '''
    load and return ollama model qwen3.5:cloud
    '''
    llm = ChatOllama(model='qwen3.5:cloud')

    return llm