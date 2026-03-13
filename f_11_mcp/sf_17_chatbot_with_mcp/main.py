from tools import load_search_tool, calculator, get_stock_price
from model import load_model, load_huggingface_model
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from state_schema import ChatState
from chat_node import chat_node
import asyncio

tools_list = [load_search_tool, calculator, get_stock_price]

model = load_huggingface_model()

llm_with_tools = model.bind_tools(tools_list)

tool_node = ToolNode(tools=tools_list)



def build_graph():

    graph = StateGraph(state_schema=ChatState)

    graph.add_node('chat_node', chat_node)

    graph.add_node('tools', tool_node)

    graph.add_edge(START, 'chat_node')

    graph.add_conditional_edges('chat_node', tools_condition)

    graph.add_edge('tools', 'chat_node')

    graph.add_edge('chat_node', END)

    workflow = graph.compile()

    return workflow

async def main():

    chatboat = build_graph()
    prompt = input("Enter your prompt: ")
    initial_state = {
    'model': llm_with_tools,
    'messages': [
        {'role': 'user', 'content': prompt}
    ]
    }

    result = await chatboat.ainvoke(initial_state)
    print(f"Result: {result['messages'][-1].content}")

if __name__=='__main__':
    asyncio.run(main())