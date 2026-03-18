import os
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import dotenv_values

# 1. Load the .env file if you are using one
env_vars = dotenv_values('.env')

HUGGINGFACEHUB_API_TOKEN = env_vars.get('HUGGINGFACEHUB_API_TOKEN')
# The API key will be automatically picked up from the environment variable (HF_API_TOKEN)
# Alternatively, you can pass it directly via the api_key parameter:
embeddings = HuggingFaceEndpointEmbeddings(
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
    model="google/embeddinggemma-300m"
)



# Text to embed
text = "This is a test document to embed."

# Embed a single query
query_result = embeddings.embed_query(text)
print(f"Embedding length for a single query: {len(query_result)}")

# Embed multiple documents
documents = [
    "This is the first document.",
    "This is the second document.",
    "This is a third piece of text."
]
doc_results = embeddings.embed_documents(documents)
print(f"Embedding length for documents: {len(doc_results[0])}")
