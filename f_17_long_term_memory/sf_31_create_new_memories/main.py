from langchain_ollama import ChatOllama
from langgraph.store.memory import InMemoryStore
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.store.base import BaseStore
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import HumanMessage, SystemMessage

model = ChatOllama(model="qwen3.5:cloud")

model_structured = model.with_structured_output(method='function_calling')

store = InMemoryStore()

user_id = 'u1'

user_details = ("user", user_id, "details")

memories = [
    (user_details, "profile_1", {'data': "Name: Mani"}),
    (user_details, "profile_2", {'data': "Age: 25"}),
    (user_details, "profile_3", {'data': "BSCS Graduate"}),
    (user_details, "preference_1", {'data': "Preference: Simple and concise answers."}),
    (user_details, "preference_2", {'data': "Preference: Code in python preferred."}),
    (user_details, "project", {'data': "Project: Building a personal assistant using langchain and langgraph with mcp, rag and long term memory."})
]

for namespace, key, value in memories:
    store.put(namespace, key, value)

SYSTEM_PROMPT_TEMPLATE = """You are a helpful assistant with memory capabilities.
If user-specific memory is available, use it to personalize
your responses based on what you know about the user.

Your goal is to provide relevant, friendly, and tailored
assistance that reflects the user’s preferences, context, and past interactions.

If the user’s name or relevant personal context is available, always personalize your responses by:
    – Always Address the user by name (e.g., "Sure, Nitish...") when appropriate
    – Referencing known projects, tools, or preferences (e.g., "your MCP  server python based project")
    – Adjusting the tone to feel friendly, natural, and directly aimed at the user

Avoid generic phrasing when personalization is possible. For example, instead of "In TypeScript apps..."
say "Since your project is built with TypeScript..."

Use personalization especially in:
    – Greetings and transitions
    – Help or guidance tailored to tools and frameworks the user uses
    – Follow-up messages that continue from past context

Always ensure that personalization is based only on known user details and not assumed.

In the end suggest 3 relevant further questions based on the current response and user profile

The user’s memory (which may be empty) is provided as: {user_details_content}
"""

def chat_node(state: MessagesState, config: RunnableConfig, store: BaseStore):

    user_id = config['configurable']['user_id']

    user_details = ("user", user_id, "details")

    items = store.search(user_details)

    if items:
        user_details_content = "\n".join([item.value.get('data', '') for item in items])

    else:
        user_details_content = ""

    system_prompt = SYSTEM_PROMPT_TEMPLATE.format(user_details_content=user_details_content)

    system_message = SystemMessage(content=system_prompt)

    response = model.invoke([system_message] + state['messages'])

    return {
        'messages':[response]
    }

graph = StateGraph(MessagesState)

graph.add_node('chat', chat_node)

graph.add_edge(START, 'chat')
graph.add_edge('chat', END)

workflow = graph.compile(store=store)

config = {
    'configurable': {
        'user_id': 'u1'
    }
}

if __name__ == "__main__":

    result = workflow.invoke({
        'messages': [HumanMessage(content="What do you know about me?")]
    },config=config)

    print(result['messages'][-1].content)