from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import RemoveMessage

model = ChatOllama(model='qwen3.5:cloud')

class ChatState(MessagesState):
    summary: str

def chat_node(state: ChatState):

    messages = []
    summary = state['summary']

    if summary:
        messages.append(
            ('system', f"Summary of previous conversation: {summary}")
        )

    messages.extend(state['messages'])

    response = model.invoke(messages)

    return {
        'messages': [response]
    }

def summarize_conversation(state: ChatState):

    existing_summary = state.get('summary', '')

    if existing_summary:
        prompt =(
            f"Existing summary: {existing_summary}\n"
            "Extend the summary using the new conversation above."
        )
    else:
        prompt = "Write a summary of the conversation above."

    messages_for_summary = state['messages'] + [('user', prompt)]

    response = model.invoke(messages_for_summary)

    messages_to_delete = state['messages'][:-2]

    return {
        'summary': response.content,
        'messages': [RemoveMessage(id=m.id) for m in messages_to_delete]
    }

def should_summarize(state: ChatState):
    return len(state['messages']) > 5

graph = StateGraph(ChatState)

graph.add_node('chat', chat_node)
graph.add_node('summarize', summarize_conversation)

graph.add_edge(START, 'chat')
graph.add_conditional_edges('chat', should_summarize, {True: 'summarize', False: END})
graph.add_edge('summarize', END)

checkpointer = InMemorySaver()

workflow = graph.compile(checkpointer=checkpointer)

config = {'configurable':{'thread_id':'chat_1'}}

initial_state = {
    'messages' : [
        ('user', 'Write a blog on ai')
    ],
    'summary': ''
}


if __name__=="__main__":
    # running multiple times to see the effect of deletion of messages
    workflow.invoke(input={'messages':[('user','what is ai')], 'summary': ''}, config=config)
    workflow.invoke(input={'messages':[('user','what is ds')], 'summary': ''}, config=config)
    workflow.invoke(input={'messages':[('user','what is cs')], 'summary': ''}, config=config)
    workflow.invoke(input={'messages':[('user','what is dl')], 'summary': ''}, config=config)
    workflow.invoke(input={'messages':[('user','what is ml')], 'summary': ''}, config=config)
    workflow.invoke(input={'messages':[('user','what is api')], 'summary': ''}, config=config)
    workflow.invoke(input={'messages':[('user','what is mcp')], 'summary': ''}, config=config)
    workflow.invoke(input={'messages':[('user','what is llm')], 'summary': ''}, config=config)
    workflow.invoke(input={'messages':[('user','what is nlp')], 'summary': ''}, config=config)
    workflow.invoke(input={'messages':[('user','what is gen ai')], 'summary': ''}, config=config)

    state = workflow.get_state(config)
    summary = state.values['summary']
    msgs = state.values['messages']
    print()
    print(f"Length of summary: {len(summary)}")
    print()
    print(f"Length of messages: {len(msgs)}")
    print()

    print(f"All messages")

    for i, msg in enumerate(msgs):
        print(f"Message {i}: {msg.content}")
        print()