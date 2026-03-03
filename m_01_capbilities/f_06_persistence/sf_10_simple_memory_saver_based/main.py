from generate_joke import generate_joke
from generate_joke_explanation import generate_joke_explanation
from model import load_model
from state_schema import JokeState
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver

model = load_model()

graph = StateGraph(state_schema=JokeState)

graph.add_node('joke', generate_joke)
graph.add_node('explanation', generate_joke_explanation)

graph.add_edge(START, 'joke')
graph.add_edge('joke', 'explanation')
graph.add_edge('explanation', END)

checkpointer = InMemorySaver()

workflow= graph.compile(checkpointer=checkpointer)

config1 = {
  'configurable':{'thread_id':'1'}
}

initial_state = {'topic':"Data", 'model':model}

result = workflow.invoke(input=initial_state, config=config1)

# print(workflow.get_state(config1))

state_history = list(workflow.get_state_history(config1))

# print(state_history[-3])

# for key, val in result.items():
#   print()
#   print(f"----------{key.capitalize()}-----------")
#   print(val)