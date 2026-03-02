from typing import TypedDict, Annotated, Any
from langgraph.graph.message import AnyMessage, add_messages

class ChatState(TypedDict):
    '''
    This is the state schema for the chatbot workflow. It defines the structure of the state that will be passed between the nodes in the workflow.
    '''
    model: Any
    messages: Annotated[list[AnyMessage], add_messages]