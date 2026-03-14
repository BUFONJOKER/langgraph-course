def retrieve(vector_store):
    '''This function create retriever from vector store'''
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    return retriever