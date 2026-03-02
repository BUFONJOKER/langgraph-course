from batsmen_state import BatsmenState
from calculate_balls_per_boundary import balls_per_boundary
from calculate_boundary_percent import boundary_percent
from calculate_strike_rate import strike_rate
from calculate_summary import summary
from langgraph.graph import START, END, StateGraph

graph = StateGraph(state_schema=BatsmenState)

graph.add_node('calculate_balls_per_boundary', balls_per_boundary)
graph.add_node('calculate_boundary_percent', boundary_percent)
graph.add_node('calculate_strike_rate', strike_rate)
graph.add_node('calculate_summary', summary)

graph.add_edge(start_key=START, end_key='calculate_balls_per_boundary')
graph.add_edge(start_key=START, end_key='calculate_boundary_percent')
graph.add_edge(start_key=START, end_key='calculate_strike_rate')

graph.add_edge(
    start_key='calculate_balls_per_boundary', end_key='calculate_summary'
)
graph.add_edge(
    start_key='calculate_boundary_percent',end_key='calculate_summary'
)
graph.add_edge(start_key='calculate_strike_rate', end_key='calculate_summary')

graph.add_edge(start_key='calculate_summary', end_key=END)

workflow = graph.compile()

input_state = {
    'runs': 100,
    'balls': 37,
    'fours': 10,
    'sixes': 5
}


result = workflow.invoke(input=input_state)

print(result)