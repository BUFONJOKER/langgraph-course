from generate_joke import generate_joke
from generate_joke_explanation import generate_joke_explanation
from model import load_model
from state_schema import JokeState
from langgraph.graph import StateGraph, START, END

model = load_model()

graph = StateGraph(state_schema=JokeState)

graph.add_node('joke', generate_joke)
graph.add_node('explanation', generate_joke_explanation)

graph.add_edge(START, 'joke')
graph.add_edge('joke', 'explanation')
graph.add_edge('explanation', END)

workflow = graph.compile()



initial_state = {'topic':"Data", 'model':model}

result = workflow.invoke(input=initial_state)

for key, val in result.items():
  print()
  print(f"----------{key.capitalize()}-----------")
  print(val)