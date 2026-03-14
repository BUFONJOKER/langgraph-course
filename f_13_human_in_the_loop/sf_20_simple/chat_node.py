from langchain_core.messages import AIMessage
from chat_state import ChatState
from langgraph.types import interrupt

def chat_node(state: ChatState) -> dict:

    '''A node that generates a response from the model, but first asks for human approval.'''

    decision = interrupt({
        'type':'approval',
        'reason':'Model is about to generate a response. Do you want to allow it?',
        'question':state['messages'][-1].content,
        'instruction':'Approve or reject the model response.'
    })

    if decision['approved'] == 'no':

        return {'messages':[AIMessage(content='Not approved by human.')]}

    else:

        response = state['model'].invoke(state['messages'])

        return {'messages':[response]}