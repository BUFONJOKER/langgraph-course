from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(document):

    splitter = RecursiveCharacterTextSplitter(chuk_size=1000, chunk_overlap=200)

    chunks = splitter.split_documents(documents=document)

    return chunks