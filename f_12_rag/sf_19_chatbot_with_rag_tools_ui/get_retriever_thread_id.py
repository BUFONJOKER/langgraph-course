from typing import Optional, Any
from retriever_state import RETRIEVER_STATE


def get_retriever_thread_id(thread_id: Optional[str], retrievers: Optional[dict[str, Any]] = None):
    '''Get retriever by thread id from shared memory store.'''

    if not thread_id:
        return None

    stores = []
    if retrievers is not None:
        stores.append(retrievers)
    stores.append(RETRIEVER_STATE['thread_retrievers'])
    for store in stores:
        if thread_id in store:
            return store[thread_id]

    return None