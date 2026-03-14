from typing import TypedDict
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
import streamlit as st

model = ChatOllama(model='qwen3.5:cloud')

class SubGraphState(TypedDict):
    input_text: str
    urdu_text: str

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

    response = subgraph_workflow.invoke({'input_text':state['eng_answer']})

    return {
        'urdu_answer':response['urdu_text']
    }

def urdu_text(state: SubGraphState):

    prompt = f'''Translate this english text  into urdu \n
    English Text -- {state['input_text']}'''

    response= model.invoke(prompt)

    return {
        'urdu_text':response.content
    }

graph = StateGraph(GraphState)


graph.add_node("chat",chat)
graph.add_node('translate', translate)


graph.add_edge(START, 'chat')
graph.add_edge('chat', 'translate')
graph.add_edge('translate', END)

graph_workflow = graph.compile()


subgraph = StateGraph(SubGraphState)
subgraph.add_node('urdu_text', urdu_text)

subgraph.add_edge(START, 'urdu_text')
subgraph.add_edge('urdu_text', END)


subgraph_workflow = subgraph.compile()


question = "What is AI?"

result = graph_workflow.invoke({'question':question})

st.markdown(result['question'])
st.divider()
st.markdown(result['eng_answer'])
st.divider()
st.markdown(result['urdu_answer'])