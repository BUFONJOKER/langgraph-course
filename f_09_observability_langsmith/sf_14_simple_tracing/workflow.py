from state_schema import ChatState
from chat import generate_chat
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver
from database_connection import create_connection
import streamlit as st

conn = create_connection()

@st.cache_resource
def generate_workflow():
  '''
  This function generate workflow (start -> chat -> end) and retrieve all threads from the database.
  '''

  graph = StateGraph(state_schema=ChatState)

  graph.add_node('chat', generate_chat)

  graph.add_edge(START, 'chat')

  graph.add_edge('chat', END)

  checkpointer = SqliteSaver(conn=conn)

  # Create the required database tables if they don't exist
  checkpointer.setup()

  workflow = graph.compile(checkpointer=checkpointer)

  # Query the correct table name (checkpoints, not chatbot_checkpoints)
  all_threads = [thread_id for thread_id, in conn.execute("SELECT DISTINCT thread_id FROM checkpoints").fetchall()]

  return workflow, all_threads