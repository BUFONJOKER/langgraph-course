from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import RemoveMessage

model = ChatOllama(model='qwen3.5:cloud')

def call_model(state: MessagesState):
    # trim messages to fit within token limit
    response = model.invoke(state['messages'])
    return {
        'messages': [response]
    }

def delete_msgs(state: MessagesState):
    # keep last 5 messages and delete the rest
    messages = state['messages']

    if len(messages) > 5:
        return {
            'messages':[RemoveMessage(id=m.id) for m in messages[:-5]]
        }

    return {
        'messages': []
    }

graph = StateGraph(MessagesState)

graph.add_node('chat', call_model)
graph.add_node('delete_msgs', delete_msgs)

graph.add_edge(START, 'chat')
graph.add_edge('chat', 'delete_msgs')
graph.add_edge('delete_msgs', END)

checkpointer = InMemorySaver()

workflow = graph.compile(checkpointer=checkpointer)

config = {'configurable':{'thread_id':'chat_1'}}

initial_state = {
    'messages' : [
        ('user', 'Write a blog on ai')
    ]
}


if __name__=="__main__":
    # running multiple times to see the effect of deletion of messages
    workflow.invoke(input={'messages':[('user','what is ai')]}, config=config)
    workflow.invoke(input={'messages':[('user','what is ds')]}, config=config)
    workflow.invoke(input={'messages':[('user','what is cs')]}, config=config)
    workflow.invoke(input={'messages':[('user','what is dl')]}, config=config)
    workflow.invoke(input={'messages':[('user','what is ml')]}, config=config)
    workflow.invoke(input={'messages':[('user','what is api')]}, config=config)
    workflow.invoke(input={'messages':[('user','what is mcp')]}, config=config)
    workflow.invoke(input={'messages':[('user','what is llm')]}, config=config)
    workflow.invoke(input={'messages':[('user','what is nlp')]}, config=config)
    workflow.invoke(input={'messages':[('user','what is gen ai')]}, config=config)

    state = workflow.get_state(config)
    msgs = state.values['messages']
    print()
    print(f"Length of messages: {len(msgs)}")
    print()

    print(f"All messages")

    for i, msg in enumerate(msgs):
        print(f"Message {i}: {msg.content}")
        print()