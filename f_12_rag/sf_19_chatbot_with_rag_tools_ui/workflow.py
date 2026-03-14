import streamlit as st
from state_schema import ChatState
from langgraph.prebuilt import tools_condition, ToolNode
from langgraph.graph import StateGraph, START, END
from chat_node import chat_node
from database_connection import create_connection
from langgraph.checkpoint.sqlite import SqliteSaver

conn = create_connection()


@st.cache_resource
def build_workflow(_tools_list, model):
    '''This function builds the workflow for the RAG chatbot using LangGraph. It creates a state graph with a chat node and a tool node, and defines the edges between them based on the tools_condition.'''

    checkpoint = SqliteSaver(conn=conn)

    llm_with_tools = model.bind_tools(_tools_list)

    tool_node = ToolNode(_tools_list)

    graph = StateGraph(ChatState)

    graph.add_node('chat_node', chat_node)
    graph.add_node('tools', tool_node)

    graph.add_edge(START, 'chat_node')
    graph.add_conditional_edges('chat_node', tools_condition)
    graph.add_edge('tools', 'chat_node')
    graph.add_edge('chat_node', END)

    checkpoint.setup()

    workflow = graph.compile(checkpointer=checkpoint)

    all_threads = [
        str(row[0])
        for row in conn.execute("SELECT DISTINCT thread_id FROM checkpoints").fetchall()
        if row and row[0] is not None
    ]

    return workflow, llm_with_tools, all_threads
