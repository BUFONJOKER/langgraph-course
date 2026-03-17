from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.checkpoint.postgres import PostgresSaver

model = ChatOllama(model='qwen3.5:cloud')

def chat_node(state: MessagesState):

    result = model.invoke(state['messages'])

    return {
        'messages': [result]
    }

graph = StateGraph(MessagesState)

graph.add_node('chat',chat_node)

graph.add_edge(START, 'chat')
graph.add_edge('chat', END)

database_url = 'postgresql://mani:mani@localhost:5432/short_term_memory_db'

with PostgresSaver.from_conn_string(database_url) as checkpoint:

    # run first time only to create the table
    # checkpoint.setup()

    config = {'configurable':{'thread_id': 'thread_2'}}

    workflow = graph.compile(checkpointer=checkpoint)

    initial_state = {
        'messages': [
            ('user', 'my name is rathore?')
        ]
    }

    result = workflow.invoke(initial_state, config=config)

    initial_state = {
        'messages': [
            ('user', 'What is my name?')
        ]
    }

    result = workflow.invoke(initial_state, config=config)

    state = workflow.get_state(config)
    state_values = state.values
    for m in state_values.get('messages',[]):
        print(type(m).__name__, ':', m.content)

    print()
