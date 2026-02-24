from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph

llm = ChatOllama(model='qwen3.5:397b')

print(llm)