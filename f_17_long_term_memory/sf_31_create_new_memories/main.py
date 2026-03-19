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

class MemoryDecision(BaseModel):
    should_write: bool = Field(description="Whether to write to memory or not")
    memories: List[str] = Field(default_factory=list, description="Atomic user memories to be stored if should_write is true")

model_structured = model.with_structured_output(MemoryDecision, method='function_calling')

store = InMemoryStore()

def rembeber_only_node(state: MessagesState, config: RunnableConfig, store: BaseStore):

    user_id = config['configurable']['user_id']

    name_space = ("user", user_id, "details")

    last_message = state['messages'][-1].content

    decision: MemoryDecision = model_structured.invoke(
        [
            SystemMessage(content=("Extract LONG-TERM memories from the user's message.\n"
                    "Only store stable, user-specific info (identity, preferences, ongoing projects).\n"
                    "Do NOT store transient info.\n"
                    "Return should_write=false if nothing is worth storing.\n"
                    "Each memory should be a short atomic sentence.")),
            HumanMessage(content=last_message)
        ]
    )

    if decision.should_write:
        for memory in decision.memories:
            store.put(name_space, str(uuid.uuid4()), {'data': memory})

    return {
        'messages':SystemMessage(content="Memories updated.")
    }

graph = StateGraph(MessagesState)

graph.add_node('remember_only', rembeber_only_node)

graph.add_edge(START, 'remember_only')
graph.add_edge('remember_only', END)

workflow = graph.compile(store=store)

config = {'configurable': {'user_id': 'u1'}}

result = workflow.invoke({
    'messages': [HumanMessage(content="I am learning genertive ai?")]
},config=config)

items = store.search(('user','u1','details'))

for item in items:
    print(item.value['data'])