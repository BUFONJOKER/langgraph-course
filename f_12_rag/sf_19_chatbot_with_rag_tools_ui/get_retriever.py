from document_loader import load_pdf
from document_splitter import split_documents
from generate_embeddings import embeddings
from retriever import retrieve
import streamlit as st
from model import load_embeddings_model

embeddings_model = load_embeddings_model(model_name="sentence-transformers/all-MiniLM-L6-v2")

@st.cache_resource
def get_retriever(file_path):
    # Load the PDF document
    documents = load_pdf(file_path)

    # split the document into smaller chunks
    chunks = split_documents(documents)

    # Generate embeddings for the document chunks and create a vector store
    vector_store = embeddings(embeddings_model, chunks)

    # Create a retriever from the vector store
    retriever = retrieve(vector_store)

    st.session_state['retriever'] = retriever

    return retriever, documents, chunks