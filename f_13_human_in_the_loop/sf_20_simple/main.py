from model import load_model
from langgraph.graph import StateGraph, START, END
from chat_state import ChatState
from chat_node import chat_node
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage
from langgraph.types import Command
# import streamlit as st

# st.header("Human in the Loop Example")

model = load_model()

graph = StateGraph(state_schema=ChatState)

graph.add_node('chat', chat_node)

graph.add_edge(START, 'chat')
graph.add_edge('chat', END)

checkpoint = MemorySaver()

workflow = graph.compile(checkpointer=checkpoint)

config = {'configurable':{'thread_id': 'thread_1'}}

# initial_state = {
#     'model':model,
#     'messages':[
#         ('user',"write a blog on aliens living in other planet far away from earth in 100 words?")
#     ]
# }

initial_state = {
    'model':model,
    'messages':[
        HumanMessage(content="what is artificial intelligence asistants?")
    ]
}

result = workflow.invoke(initial_state, config)

print()

ai_message = result['__interrupt__'][0].value

user_decision = input(f"Model is about to generate the following response: '{ai_message}'. \nDo you want to allow it? (yes/no): ")

final_result = workflow.invoke(
    Command(resume={'approved':user_decision}),
    config=config
)

print()
print(final_result['messages'][-1].content)