from tools import load_search_tool, calculator, get_stock_price
from model import load_model, load_huggingface_model
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from state_schema import ChatState
from chat_node import chat_node
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

HORIZON_TOKEN = os.getenv("HORIZON_TOKEN")

SERVERS = {
    'Calculator Tools':{
        'transport':'stdio',
        'command':'python3',
        'args':['/home/mani/data-science/langgraph-course/f_11_mcp/sf_17_chatbot_with_mcp/mcp_server.py']
    },
    "Expense Tracker MCP (Hosted)": {
        "url": "https://expensetrackerappmcp.fastmcp.app/mcp",
        "transport": "streamable_http",
        "headers": {
            "Authorization": f"Bearer {HORIZON_TOKEN}" #
        }
    }
}

client = MultiServerMCPClient(SERVERS)

model = load_model()


async def build_graph():

    mcp_tools = await client.get_tools()

    local_tools = [load_search_tool(), calculator, get_stock_price]

    # Keep a single source of truth for both model binding and tool execution.
    tools = [*mcp_tools, *local_tools]

    print(tools)


    llm_with_tools = model.bind_tools(tools)

    tool_node = ToolNode(tools=tools)

    graph = StateGraph(state_schema=ChatState)

    graph.add_node('chat_node', chat_node)

    graph.add_node('tools', tool_node)

    graph.add_edge(START, 'chat_node')

    graph.add_conditional_edges('chat_node', tools_condition)

    graph.add_edge('tools', 'chat_node')

    graph.add_edge('chat_node', END)

    workflow = graph.compile()

    return workflow, llm_with_tools

async def main():

    chatboat, llm_with_tools = await build_graph()
    prompt = input("Enter your prompt: ")
    initial_state = {
    'model': llm_with_tools,
    'messages': [
        {'role': 'user', 'content': prompt},
    ]
    }

    result = await chatboat.ainvoke(initial_state)
    print(f"Result: {result['messages'][-1].content}")

if __name__=='__main__':
    asyncio.run(main())