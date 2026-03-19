from langchain_ollama import ChatOllama
from langgraph.store.postgres import PostgresStore
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.store.base import BaseStore
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel, Field
from typing import List
import uuid


model = ChatOllama(model="qwen3.5:cloud")

class MemoryItem(BaseModel):
    text: str = Field(description="Atomic user memory as short sentence")
    is_new: bool = Field(description="True if this memory is new and false if it's an update to existing memory")

class MemoryDecision(BaseModel):
    should_write: bool = Field(description="Whether to write to memory or not")
    memories: List[MemoryItem] = Field(default_factory=list, description="Atomic user memories to be stored if should_write is true")

model_structured = model.with_structured_output(MemoryDecision, method='function_calling')

# ----------------------------
# 2) System prompt
# ----------------------------
SYSTEM_PROMPT_TEMPLATE = """You are a helpful assistant with memory capabilities.
If user-specific memory is available, use it to personalize
your responses based on what you know about the user.

Your goal is to provide relevant, friendly, and tailored
assistance that reflects the user’s preferences, context, and past interactions.

If the user’s name or relevant personal context is available, always personalize your responses by:
    – Always Address the user by name (e.g., "Sure, Nitish...") when appropriate
    – Referencing known projects, tools, or preferences (e.g., "your MCP server python based project")
    – Adjusting the tone to feel friendly, natural, and directly aimed at the user

Avoid generic phrasing when personalization is possible.

Use personalization especially in:
    – Greetings and transitions
    – Help or guidance tailored to tools and frameworks the user uses
    – Follow-up messages that continue from past context

Always ensure that personalization is based only on known user details and not assumed.

In the end suggest 3 relevant further questions based on the current response and user profile

The user’s memory (which may be empty) is provided as: {user_details_content}
"""

MEMORY_PROMPT = """You are responsible for updating and maintaining accurate user memory.

CURRENT USER DETAILS (existing memories):
{user_details_content}

TASK:
- Review the user's latest message.
- Extract user-specific info worth storing long-term (identity, stable preferences, ongoing projects/goals).
- For each extracted item, set is_new=true ONLY if it adds NEW information compared to CURRENT USER DETAILS.
- If it is basically the same meaning as something already present, set is_new=false.
- Keep each memory as a short atomic sentence.
- No speculation; only facts stated by the user.
- If there is nothing memory-worthy, return an empty list.
"""

def rembeber_node(state: MessagesState, config: RunnableConfig, store: BaseStore):

    user_id = config['configurable']['user_id']

    name_space = ("user", user_id, "details")

    # load existing memories for the user
    existing_items = store.search(name_space)

    existing_text = [item.value.get('data','') for item in existing_items if item.value.get('data')]

    user_details_content = "\n".join(f" - {text}" for text in existing_text) if existing_text else "No existing memories."

    last_message = state['messages'][-1].content

    decision: MemoryDecision = model_structured.invoke(
        [
            SystemMessage(content=MEMORY_PROMPT.format(user_details_content=user_details_content)),
            HumanMessage(content=last_message)
        ]
    )

    if decision.should_write:
        for memory in decision.memories:
            if isinstance(memory, MemoryItem):
                if memory.is_new and memory.text:
                    store.put(name_space, str(uuid.uuid4()), {'data': memory.text})
            elif isinstance(memory, str) and memory.strip():
                # Fallback in case the model emits plain strings despite the schema.
                store.put(name_space, str(uuid.uuid4()), {'data': memory.strip()})

    return {
        'messages':SystemMessage(content="Memories updated.")
    }


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

graph.add_node('remember_only', rembeber_node)
graph.add_node('chat', chat_node)

graph.add_edge(START, 'remember_only')
graph.add_edge('remember_only', 'chat')
graph.add_edge('chat', END)


database_url = 'postgresql://mani:mani@localhost:5432/short_term_memory_db'

with PostgresStore.from_conn_string(database_url) as store:

    # run only first time to create the table in postgres, after that you can comment it out
    # store.setup()

    workflow = graph.compile(store=store)

    config = {
        'configurable': {
            'user_id': 'u1'
        }
    }


    # result = workflow.invoke({
    #     'messages': [HumanMessage(content="I am learning genertive ai?")]
    # },config=config)

    # result = workflow.invoke({
    #     'messages': [HumanMessage(content="My name is mani?")]
    # },config=config)

    # print(result['messages'][-1].content)

    items = store.search(('user','u1','details'))

    print("\nMemories stored in Postgres:")

    for item in items:
        print(item.value['data'])