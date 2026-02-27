from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

def load_ollama_model():
    '''
    Load ollama qwen3-next:80b-cloud model
    '''
    model = ChatOllama(model='qwen3-next:80b-cloud')
    return model

def load_huggingface_model():
    '''
    Load HuggingFace model meta-llama/Llama-3.1-8B-Instruct for text generation task
    '''

    llm = HuggingFaceEndpoint(
        repo_id = "meta-llama/Llama-3.1-8B-Instruct",
        task = "text-generation",
    )

    model = ChatHuggingFace(llm=llm)

    return model