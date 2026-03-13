from langchain_ollama import ChatOllama
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

def load_model():
	'''Load the Ollama model qwen3.5:cloud'''

	model = ChatOllama(model="qwen3.5:cloud")

	return model

def load_huggingface_model():
	'''this function load the huggingface model'''

	llm = HuggingFaceEndpoint(repo_id='Qwen/Qwen3.5-397B-A17B')

	model = ChatHuggingFace(llm=llm)

	return model
