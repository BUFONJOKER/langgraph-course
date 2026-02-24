from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

def load_model():
    llm = HuggingFaceEndpoint(repo_id='Qwen/Qwen3.5-397B-A17B')

    model = ChatHuggingFace(llm=llm)
    
    return model
