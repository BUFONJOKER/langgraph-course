from typing import TypedDict, Any, Annotated
from langgraph.graph.message import add_messages, AnyMessage
from pydantic import Field

class ChatState(TypedDict):
  '''
  This class ChatState is state schema with two variables model and messages.
  '''

  model: Any = Field(None, description="LLM used for responses")
  
  messages: Annotated[list[AnyMessage], add_messages] = Field(None, description="List of conversation messages")