from state_schema import ChatState

def chat_node(state: ChatState) -> dict:
  '''
  This function generate responses from llm according to given prompt.
  '''

  model = state['model']

  messages = state['messages']

  response = model.invoke(messages)

  return {'messages':[response]}