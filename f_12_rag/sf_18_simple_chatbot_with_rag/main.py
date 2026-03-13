from document_loader import load_pdf
from document_splitter import split_documents
from generate_embeddings import embeddings
from retriever import retrieve
from model import load_embeddings_model, load_model

embeddings_model = load_embeddings_model(model_name="sentence-transformers/all-MiniLM-L6-v2")

model = load_model(model_name="qwen3.5:cloud")

file_path = 'intro-to-ml.pdf'

# Load the PDF document
documents = load_pdf(file_path)

# split the document into smaller chunks
split_docs = split_documents(documents)

# Generate embeddings for the document chunks and create a vector store
vector_store = embeddings(embeddings_model, split_docs)

# Create a retriever from the vector store
retriever = retrieve(vector_store)
