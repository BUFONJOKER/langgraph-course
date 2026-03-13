from state_schema import ChatState
import asyncio

async def chat_node(state: ChatState) -> dict:
  '''
  This function generate responses from llm according to given prompt.
  '''

  model = state['model']

  messages = state['messages']

  response = await model.ainvoke(messages)

  return {'messages':[response]}