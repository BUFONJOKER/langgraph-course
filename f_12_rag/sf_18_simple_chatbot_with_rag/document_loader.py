from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path):
    '''This function load pdf using using document loader PyPDFLoader'''

    loader = PyPDFLoader(file_path)

    documents = loader.load()

    return documents