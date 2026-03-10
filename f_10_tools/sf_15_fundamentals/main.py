from tools import load_search_tool, calculator, get_stock_price
from model import load_model
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from state_schema import ChatState
from chat_node import chat_node
import streamlit as st
from dotenv import load_dotenv
import os

os.environ['LANGSMITH_PROJECT'] = 'Tools Fundamentals'

# load_dotenv()

tools_list = [load_search_tool, calculator, get_stock_price]

model = load_model()

llm_with_tools = model.bind_tools(tools_list)

tool_node = ToolNode(tools=tools_list)

graph = StateGraph(state_schema=ChatState)

graph.add_node('chat_node', chat_node)

graph.add_node('tools', tool_node)

graph.add_edge(START, 'chat_node')

graph.add_conditional_edges('chat_node', tools_condition)

graph.add_edge('tools', 'chat_node')

graph.add_edge('chat_node', END)

workflow = graph.compile()

initial_state = {
  'model': llm_with_tools,
  'messages': [
    {'role': 'user', 'content': 'what is 65878999*369858/9555665-5544442+4468977?'}
  ]
}

result = workflow.invoke(initial_state)

st.write(result['messages'][-1].content)
