from langchain_ollama import ChatOllama

def load_model():
  '''
  This function load qwen3-next:80b-cloud ollama model.
  '''

  model = ChatOllama(model='qwen3-next:80b-cloud')

  return model