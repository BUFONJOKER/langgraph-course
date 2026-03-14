from typing import Optional
import tempfile
from get_retriever import get_retriever
import os
from retriever_state import RETRIEVER_STATE

def ingest_pdf(file_bytes: bytes, thread_id: str, filename: Optional[str] = None):
    '''
    Build a FAISS retriever for the uploaded pdf and store it for the thread.
    Returns a summary dict that can be surfaced in the ui
    '''

    if not file_bytes:
        raise ValueError("No bytes received in this ingestion")

    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
        temp_file.write(file_bytes)
        temp_path = temp_file.name

    try:
        retriever, documents, chunks = get_retriever(temp_path)

        thread_id_str = str(thread_id)

        RETRIEVER_STATE['thread_retrievers'][thread_id_str] = retriever

        metadata = {
            'filename': filename or os.path.basename(temp_path),
            'documents':len(documents),
            'chunks':len(chunks)
        }

        RETRIEVER_STATE['thread_metadata'][thread_id_str] = metadata

        output = {
            'filename': filename or os.path.basename(temp_path),
            'documents':len(documents),
            'chunks':len(chunks)
        }

        return output
    finally:
         # The FAISS store keeps copies of the text, so the temp file is safe to remove.
        try:
            os.remove(temp_path)
        except OSError:
            pass