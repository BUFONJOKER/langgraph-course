from state_schema import ChatState
from chat import generate_chat
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
import streamlit as st


@st.cache_resource
def generate_workflow():
  '''
  This function generate workflow start -> chat -> end.
  '''

  graph = StateGraph(state_schema=ChatState)

  graph.add_node('chat', generate_chat)

  graph.add_edge(START, 'chat')

  graph.add_edge('chat', END)

  checkpointer = InMemorySaver()

  workflow = graph.compile(checkpointer=checkpointer)

  return workflow