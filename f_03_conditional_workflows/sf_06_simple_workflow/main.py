from calculate_discriminant import calculate_discriminant
from calculate_roots import calculate_roots
from complex_roots import complex_roots
from distinct_roots import distinct_roots
from repeated_root import repeated_root
from show_equation import show_equation
from state_schema import QuadraticState
from langgraph.graph import StateGraph, START, END

graph = StateGraph(QuadraticState)

graph.add_node('show_equation', show_equation)
graph.add_node('calculate_discriminant', calculate_discriminant)

graph.add_node('complex_roots', complex_roots)
graph.add_node('distinct_roots', distinct_roots)
graph.add_node('repeated_root', repeated_root)

graph.add_edge(START, 'show_equation')
graph.add_edge('show_equation', 'calculate_discriminant')

graph.add_conditional_edges('calculate_discriminant', calculate_roots)

graph.add_edge('complex_roots', END)
graph.add_edge('distinct_roots', END)
graph.add_edge('repeated_root', END)

workflow = graph.compile()

a = 1; b = 2; c = 5

input_state = {
    'a':a,
    'b':b,
    'c':c
}


result = workflow.invoke(input_state)

print(result)
