from langchain_ollama import ChatOllama
from langgraph.store.memory import InMemoryStore
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

store = InMemoryStore()

def chat_create_memory_node(state: MessagesState, config: RunnableConfig, store: BaseStore):

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

graph = StateGraph(MessagesState)

graph.add_node('chat_create_memory', chat_create_memory_node)

graph.add_edge(START, 'chat_create_memory')
graph.add_edge('chat_create_memory', END)

workflow = graph.compile(store=store)

config = {'configurable': {'user_id': 'u1'}}

result = workflow.invoke({
    'messages': [HumanMessage(content="I am learning genertive ai?")]
},config=config)

# items = store.search(('user','u1','details'))

# for item in items:
#     print(item.value['data'])

# check if duplicate memory is added or not
result = workflow.invoke({
    'messages': [HumanMessage(content="my name is mani?")]
},config=config)

# items = store.search(('user','u1','details'))

# for item in items:
#     print(item.value['data'])

result = workflow.invoke({
    'messages': [HumanMessage(content="I am learning genertive ai?")]
},config=config)

items = store.search(('user','u1','details'))

for item in items:
    print(item.value['data'])