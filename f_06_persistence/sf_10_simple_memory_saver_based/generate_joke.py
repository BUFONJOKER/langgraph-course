from state_schema import JokeState
from langchain_core.prompts import ChatPromptTemplate

def generate_joke(state: JokeState) -> dict:
  '''
  This fuction generate joke using llm according to given topic
  '''

  topic = state['topic']
  model = state['model']

  SYSTEM_INSTRUCTIONS = "You are a joke generator. You generate jokes based on the given topic."
  USER_CONTENT = f'''Generate a joke based on the topic: {topic}'''

  prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_INSTRUCTIONS),
    ("user", USER_CONTENT)])

  chain = prompt | model

  joke = chain.invoke({'topic': topic})

  return {
    'joke':joke.content
  }