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
    Load HuggingFace model zai-org/GLM-4.7-Flash for text generation task
    '''

    llm = HuggingFaceEndpoint(
        repo_id = "zai-org/GLM-4.7-Flash",
        task = "text-generation",
    )

    model = ChatHuggingFace(llm=llm)

    return model