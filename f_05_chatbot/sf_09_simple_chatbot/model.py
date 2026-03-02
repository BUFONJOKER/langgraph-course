from langchain_ollama import ChatOllama

def load_model():
    '''
    This function is responsible for loading the Ollama qwen3.5:cloud model for the chatbot workflow.
    '''
    model = ChatOllama(model = 'qwen3.5:cloud')

    return model