# write code to check ollama working fine
from langchain_ollama import ChatOllama
model = ChatOllama(model="qwen3.5:cloud")
result = model.invoke("What is the capital of France?")
print(result)