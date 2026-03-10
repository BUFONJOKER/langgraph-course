from state_schema import ChatState
from chat import generate_chat
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.sqlite import SqliteSaver
from database_connection import create_connection
from langgraph.prebuilt import ToolNode, tools_condition
import streamlit as st

conn = create_connection()

@st.cache_resource
def generate_workflow(_tool_node:ToolNode):
  '''
  This function generate workflow (start -> chat -> end) and retrieve all threads from the database.
  '''

  graph = StateGraph(state_schema=ChatState)

  graph.add_node('chat_node', generate_chat)

  graph.add_node('tools', _tool_node)

  graph.add_edge(START, 'chat_node')

  graph.add_conditional_edges('chat_node', tools_condition)

  graph.add_edge('tools', 'chat_node')

  graph.add_edge('chat_node', END)

  checkpointer = SqliteSaver(conn=conn)

  # Create the required database tables if they don't exist
  checkpointer.setup()

  workflow = graph.compile(checkpointer=checkpointer)

  # Query the correct table name (checkpoints, not chatbot_checkpoints)
  all_threads = [thread_id for thread_id, in conn.execute("SELECT DISTINCT thread_id FROM checkpoints").fetchall()]

  return workflow, all_threads