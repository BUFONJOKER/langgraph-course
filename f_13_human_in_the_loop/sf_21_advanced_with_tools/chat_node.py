from model import load_model
from chat_state import ChatState
from tools_defined import get_stock_price, purchase_stock

model = load_model()

tools = [get_stock_price, purchase_stock]

llm_with_tools = model.bind_tools(tools)
def chat_node(state: ChatState) -> dict:
    '''This is the main chat node that takes the current state of the conversation, invokes the model to generate a response, and returns the updated state with the new message.'''

    response = llm_with_tools.invoke(state['messages'])

    return {
        'messages': [response]
    }