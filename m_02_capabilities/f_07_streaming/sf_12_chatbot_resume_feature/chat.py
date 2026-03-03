from state_schema import ChatState
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

def generate_chat(state: ChatState) -> dict:
  '''
  This function generate response of given prompt from llm
  '''

  messages = state['messages']

  model = state['model']

  SYSTEM_INSTRUCTIONS = '''You are helpful ai assistant which generate clear reponses on given prompt'''


  prompt = ChatPromptTemplate.from_messages(
    [
      ('system', SYSTEM_INSTRUCTIONS),
      MessagesPlaceholder(variable_name='messages')
    ]
  )

  chain = prompt | model


  response = chain.invoke({'messages':messages})

  return {
    'messages':[response]
  }