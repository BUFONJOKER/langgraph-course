from langgraph.graph import StateGraph, START, END
from llm_state_class import LLMState
from llm_question_answer import llm_qa

graph = StateGraph(state_schema=LLMState)

graph.add_node('llm_qa', llm_qa)

graph.add_edge(start_key=START, end_key='llm_qa')

graph.add_edge(start_key='llm_qa', end_key=END)

workflow = graph.compile()

question = "generate mouse picture beating cat?"

input_state = {
    'question':question
}

answer = workflow.invoke(input_state)

print(answer)