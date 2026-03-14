from typing import TypedDict
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
import streamlit as st

model = ChatOllama(model='qwen3.5:cloud')

class GraphState(TypedDict):
    question: str
    eng_answer: str
    urdu_answer: str

def chat(state:GraphState):

    prompt = f"Generate clear answer following question \n {state['question']}"

    response = model.invoke(prompt)

    return {
        'eng_answer':response.content
    }

def translate(state:GraphState):

    prompt = f'''Translate this english text  into urdu \n
    English Text -- {state['eng_answer']}'''

    response= model.invoke(prompt)

    return {
        'urdu_answer':response.content
    }

subgraph = StateGraph(GraphState)
subgraph.add_node('translate', translate)

subgraph.add_edge(START, 'translate')
subgraph.add_edge('translate', END)


subgraph_workflow = subgraph.compile()



graph = StateGraph(GraphState)


graph.add_node("chat",chat)
graph.add_node('translate', subgraph_workflow)


graph.add_edge(START, 'chat')
graph.add_edge('chat', 'translate')
graph.add_edge('translate', END)

graph_workflow = graph.compile()





question = "What is AI?"

result = graph_workflow.invoke({'question':question})

st.markdown(result['question'])
st.divider()
st.markdown(result['eng_answer'])
st.divider()
st.markdown(result['urdu_answer'])