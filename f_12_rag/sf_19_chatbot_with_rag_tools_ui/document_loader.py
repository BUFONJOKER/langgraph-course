from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path: str):
    '''This function load pdf using using document loader PyPDFLoader'''

    loader = PyPDFLoader(file_path)

    documents = loader.load()

    return documents