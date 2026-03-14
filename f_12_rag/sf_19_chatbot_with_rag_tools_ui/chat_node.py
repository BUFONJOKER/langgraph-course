from state_schema import ChatState
from langchain_core.messages import SystemMessage

def chat_node(state: ChatState, config=None):
    '''
    This is the main chat node for the chatbot workflow. It takes the current state of the chat and generates a response using the model and the tools.
    '''
    thread_id = None

    if config and isinstance(config, dict):
        thread_id = config.get('configurable', {}).get("thread_id")

    system_message = SystemMessage(
        content=(
            "You are a helpful assistant. For questions about the uploaded PDF, call "
            "the `rag_tool` and include the thread_id "
            f"`{thread_id}`. You can also use the web search, stock price, and "
            "calculator tools when helpful. If no document is available, ask the user "
            "to upload a PDF."
        )
    )
    messages = [system_message, *state["messages"]]

    model = state['model']


    response = model.invoke(messages, config=config)

    return {'messages': [response]}