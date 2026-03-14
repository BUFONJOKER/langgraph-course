from retriever_state import RETRIEVER_STATE

def thread_document_metadata(thread_id: str) -> dict:
    thread_id_str = str(thread_id)
    return RETRIEVER_STATE['thread_metadata'].get(thread_id_str, {})