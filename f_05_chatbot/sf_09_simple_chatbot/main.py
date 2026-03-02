# Import necessary modules for LangGraph workflow and Streamlit UI
from langgraph.graph import StateGraph, START
from langchain_core.messages import HumanMessage
from chat_state_schema import ChatState
from chat import chat_bot
from model import load_model
import streamlit as st

# Create a container for the chatbot header and controls
with st.container():
  st.header("Simple Chatbot with LangGraph and Streamlit")

  # Button to clear conversation history
  if st.button("Clear Conversation", type='primary'):
    st.session_state['messages'] = []
    st.rerun()  # Refresh the app to show cleared state

@st.cache_resource
def generate_workflow():
  '''
  Initialize and compile the chatbot workflow.
  Cached to avoid rebuilding on every rerun.

  Returns:
    tuple: (compiled workflow, model instance)
  '''
  # Load the Ollama LLM model
  model = load_model()

  # Create a StateGraph with ChatState schema
  graph = StateGraph(state_schema=ChatState)

  # Define nodes
  # Add the chat_bot node that handles message processing
  graph.add_node('chat_bot', chat_bot)

  # Define edges
  # Connect START to chat_bot - workflow begins with the chat_bot node
  graph.add_edge(START, 'chat_bot')

  # Compile the graph into an executable workflow
  workflow = graph.compile()

  return workflow, model

# Initialize workflow and model (cached for performance)
workflow, model = generate_workflow()

# Initialize session state for message history
# This persists across Streamlit reruns
if 'messages' not in st.session_state:
  st.session_state['messages'] = []

# Display conversation history
# Iterate through all messages and render them in chat format
for message in st.session_state['messages']:

  # Determine the role (user or assistant) based on message type
  role = "user" if isinstance(message, HumanMessage) else "assistant"

  # Render message with appropriate role styling
  with st.chat_message(role):
    st.markdown(message.content)

# Handle chat input and generate response from the chatbot workflow
if prompt := st.chat_input("Ask a question to the chatbot"):

  # Display the user's message in the chat interface
  with st.chat_message("user"):
    st.markdown(prompt)

  # Create a HumanMessage object and append to session state
  # This maintains the conversation history
  user_message = HumanMessage(content=prompt)
  st.session_state['messages'].append(user_message)

  # Show loading spinner while generating AI response
  with st.spinner("Generating response...", show_time=True):

      # Prepare input state for the workflow
      # Include both the model and full message history
      input_state = {
        'model': model,
        'messages': st.session_state['messages']
      }

      # Invoke the workflow to generate AI response
      # This runs the chat_bot node with the current state
      result = workflow.invoke(input_state)

      # Extract the latest AI message from the result
      # The result contains the full updated message list
      output = result['messages'][-1]

      # Display the AI's response in the chat interface
      with st.chat_message("assistant"):
          st.markdown(output.content)

      # Append AI response to session state for conversation continuity
      st.session_state['messages'].append(output)
