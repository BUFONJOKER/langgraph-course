from langgraph.graph import StateGraph, START, END
from bmi_state_class import BMIState
from bmi_calculate import bmi_calculate
from label_bmi import label_bmi

graph = StateGraph(state_schema=BMIState)

graph.add_node('bmi_calculate', bmi_calculate)

graph.add_node('label_bmi', label_bmi)

graph.add_edge(start_key=START, end_key='bmi_calculate')

graph.add_edge(start_key='bmi_calculate', end_key='label_bmi')

graph.add_edge(start_key='label_bmi', end_key=END)

workflow = graph.compile()

weight_kg = float(input("Enter weight in kg : "))
height_m = float(input("Enter height in meters : "))

input_state = {
    'weight_kg':weight_kg,
    'height_m':height_m
}

output_state = workflow.invoke(input=input_state)

print(output_state)
print(workflow.get_graph().draw_ascii())

