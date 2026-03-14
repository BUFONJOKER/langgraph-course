from retriever_state import RETRIEVER_STATE

def thread_has_document(thread_id: str) -> bool:
    return str(thread_id) in RETRIEVER_STATE['thread_retrievers']