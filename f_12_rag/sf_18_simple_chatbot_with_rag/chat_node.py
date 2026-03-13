from state_schema import ChatState

def chat_node(state: ChatState):
    '''
    This is the main chat node for the chatbot workflow. It takes the current state of the chat and generates a response using the model and the tools.
    '''
    model = state['model']
    messages = state['messages']

    response = model.invoke(messages)

    return {'messages': [response]}