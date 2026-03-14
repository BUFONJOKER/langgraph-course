from langchain_community.vectorstores import FAISS

def embeddings(model, chunks):
    '''This function generate embeddings and store it to vector store'''

    vector_store = FAISS.from_documents(chunks, model)

    return vector_store