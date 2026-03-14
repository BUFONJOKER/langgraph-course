from typing import Any, Dict, TypedDict


class RetrieverMetadata(TypedDict):
	filename: str
	documents: int
	chunks: int


class RetrieverState(TypedDict):
	thread_retrievers: Dict[str, Any]
	thread_metadata: Dict[str, RetrieverMetadata]


# Shared in-memory state for per-thread retrievers and metadata.
RETRIEVER_STATE: RetrieverState = {
	'thread_retrievers': {},
	'thread_metadata': {},
}
