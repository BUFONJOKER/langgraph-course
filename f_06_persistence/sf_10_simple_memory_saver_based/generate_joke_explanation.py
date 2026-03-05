from langchain_core.prompts import ChatPromptTemplate
from state_schema import JokeState

def generate_joke_explanation(state: JokeState) -> dict:
  '''
  This function generate explanation of given joke using llm.
  '''

  model = state['model']
  joke = state['joke']

  SYSTEM_INSTRUCTIONS = '''You are joke explanator. You clearly explain joke in simple way'''
  USER_CONTENT = '''Explain this joke \n {joke}'''

  prompt = ChatPromptTemplate.from_messages(
    [
      ('system', SYSTEM_INSTRUCTIONS),
      ('user', USER_CONTENT)
    ]
  )

  chain = prompt | model

  explanation = chain.invoke({'joke':joke})

  return {
    'explanation':explanation.content
  }