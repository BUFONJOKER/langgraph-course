from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

def load_ollama_model():
    '''
    Load ollama qwen3-next:80b-cloud model
    '''
    model = ChatOllama(model='qwen3-next:80b-cloud')
    return model

def load_huggingface_model():
    '''
    Load HuggingFace model openai-community/gpt2 for text generation task
    '''

    llm = HuggingFaceEndpoint(
        repo_id = "openai-community/gpt2",
        task = "text-generation",
    )

    model = ChatHuggingFace(llm=llm)

    return model