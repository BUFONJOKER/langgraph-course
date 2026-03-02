from langchain_ollama import ChatOllama

def load_model():
    '''
    Load ollama qwen3-next:80b-cloud model
    '''
    model = ChatOllama(model='qwen3-next:80b-cloud')
    return model