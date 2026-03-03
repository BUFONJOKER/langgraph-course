from typing import TypedDict, Any

class JokeState(TypedDict):
  '''
  This class JokeState defines the structure of the state in a joke generation workflow.
  It contains the topic of the joke, the joke itself,an explanation of the joke and llm.
  '''

  topic: str
  joke: str
  explanation: str
  model: Any