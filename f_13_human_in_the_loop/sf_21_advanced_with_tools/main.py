
from langgraph.graph import StateGraph, START, END
from chat_state import ChatState
from chat_node import chat_node
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage
from langgraph.types import Command
from langgraph.prebuilt import ToolNode, tools_condition
from tools_defined import get_stock_price, purchase_stock
# import streamlit as st

# st.header("Human in the Loop Example")



tools = [get_stock_price, purchase_stock]

tool_node = ToolNode(tools)



graph = StateGraph(state_schema=ChatState)

graph.add_node('chat', chat_node)
graph.add_node('tools', tool_node)

graph.add_edge(START, 'chat')
graph.add_conditional_edges('chat', tools_condition)
graph.add_edge('tools','chat')
graph.add_edge('chat', END)


checkpoint = MemorySaver()

workflow = graph.compile(checkpointer=checkpoint)
print("Hello to your Personal Chatbot Ask Anything to chatbot")
print('write exit to cancel')
while True:
    prompt = input("You : ")

    if prompt == 'exit':
        break

    config = {'configurable':{'thread_id': 'thread_1'}}

    initial_state = {

        'messages':[
            HumanMessage(content=prompt)
        ]
    }

    result = workflow.invoke(initial_state, config)

    if result.get("__interrupt__"):
        interrupts = result['__interrupt__']
        user_decision = input(f"Your Decision : {interrupts[0].value}  ")

        final_result = workflow.invoke(
            Command(resume=user_decision),
            config=config
        )

        print()
        print(final_result['messages'][-1].content)

    else:

        print(f"AI : {result['messages'][-1].content} ")