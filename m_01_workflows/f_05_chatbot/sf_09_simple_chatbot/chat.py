from chat_state_schema import ChatState

def chat_bot(state: ChatState) -> dict:
    '''
    This function is responsible for generating a response based on the conversation history using LLM qwen3.5:cloud model from Ollama.
    '''
    messages = state['messages']
    # Here you would  call your LLM to generate a response based on the conversation history.

    model = state['model']

    response = model.invoke(messages)

    return {
        "messages": [response]
    }