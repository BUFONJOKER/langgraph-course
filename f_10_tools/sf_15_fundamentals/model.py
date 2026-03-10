from langchain_ollama import ChatOllama

def load_model():
  '''Load the Ollama model qwen3.5:cloud'''

  model = ChatOllama(model="qwen3.5:cloud")

  return model