from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages.utils import trim_messages, count_tokens_approximately

model = ChatOllama(model='qwen3.5:cloud')

MAX_TOKEN = 100

def call_model(state: MessagesState):
    # trim messages to fit within token limit

    messages = trim_messages(
        state['messages'],
        strategy='last',
        token_counter=count_tokens_approximately,
        max_tokens=MAX_TOKEN
    )

    print(f"Current token count: {count_tokens_approximately(messages)}")

    for msg in messages:
        print(msg.content)

    response = model.invoke(messages)

    return {
        'messages' : [response]
    }

graph = StateGraph(MessagesState)

graph.add_node('chat', call_model)

graph.add_edge(START, 'chat')
graph.add_edge('chat', END)

checkpointer = InMemorySaver()

workflow = graph.compile(checkpointer=checkpointer)

config = {'configurable':{'thread_id':'chat_1'}}

initial_state = {
    'messages' : [
        ('user', 'Write a blog on ai')
    ]
}

# result = workflow.invoke(initial_state, config=config)

# print(result)