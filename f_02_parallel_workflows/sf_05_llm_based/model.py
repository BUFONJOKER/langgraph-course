from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
load_dotenv()

def load_model():
    '''
    load model qwen3-next:80b-cloud using ollama
    '''
    llm = ChatOllama(model='qwen3-next:80b-cloud', format='json')

    # model = HuggingFaceEndpoint(
    # repo_id='Qwen/Qwen2-7B-instruct',
    # task='text-generation',
    # )

    # chatbot = ChatHuggingFace(llm=model)

    return llm





