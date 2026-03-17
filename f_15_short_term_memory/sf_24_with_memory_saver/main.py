from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.checkpoint.memory import InMemorySaver

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

# short term memory saver which save memory only in RAM and will be lost once the program is stopped. This is useful for testing and debugging.
checkpoint = InMemorySaver()

config = {'configurable':{'thread_id': 'thread_1'}}

workflow = graph.compile(checkpointer=checkpoint)

initial_state = {
    'messages': [
        ('user', 'my name is mani?')
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
