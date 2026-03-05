# ----- Chatbot Application with Conversation Memory using Streamlit and LangGraph -----



# ============================================================================
# IMPORT necessary libraries and functions for the chatbot application
# ============================================================================
from model import load_model
from workflow import generate_workflow
from langchain_core.messages import HumanMessage, AIMessage
from thread_id import generate_thread_id
from reset_chat import reset_chat
from add_thread import add_thread
from load_conversation import load_conversation
import streamlit as st

# app icon and title setup
st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")
st.title("Chatbot with Conversation Memory")

# ============================================================================
# INITIALIZE MODEL & WORKFLOW
# ============================================================================
model = load_model()
workflow = generate_workflow()


# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================
# thread_id persists across reruns, enabling conversation memory across sessions
if 'thread_id' not in st.session_state:
  st.session_state['thread_id'] = generate_thread_id()

if 'messages' not in st.session_state:
  st.session_state['messages'] = []

if 'chat_threads' not in st.session_state:
  st.session_state['chat_threads'] = []

add_thread(st.session_state['thread_id'])  # Ensure current thread_id is tracked in session state

# ============================================================================
# UI SETUP of sidebar and main chat interface
# ============================================================================

st.sidebar.title('Chatbot')
st.sidebar.header("My Conversations")

if st.sidebar.button("New Chat"):
  reset_chat()  # Clear chat history and generate new thread_id for a fresh conversation

# display all thread_ids
for thread_id in st.session_state['chat_threads'][::-1]:  # Show most recent threads at the top

  if st.sidebar.button(thread_id):

    st.session_state['thread_id'] = thread_id  # Update current thread_id to selected one
    messages = load_conversation(thread_id, workflow)  # Load conversation history for selected thread_id

    # check in messages if it is a HumanMessage or AIMessage and create a new list of messages with the same type but only content for display
    tmp_message = [type(message)(content=message.content) for message in messages]

    st.session_state['messages'] = tmp_message  # Update session state with loaded messages for display



# ============================================================================
# DISPLAY CHAT HISTORY
# ============================================================================
for message in st.session_state['messages']:
  role = 'user' if isinstance(message, HumanMessage) else 'assistant'
  with st.chat_message(role):
    st.markdown(message.content)




# ============================================================================
# HANDLE USER INPUT & GENERATE RESPONSE
# ============================================================================
if prompt := st.chat_input("Ask anything to AI assistant"):
  # Display user message
  with st.chat_message('user'):
    st.markdown(prompt)

  user_message = HumanMessage(content=prompt)
  st.session_state['messages'].append(user_message)

  # Generate AI response
  with st.chat_message('assistant'):
    with st.spinner("Generating response...", show_time=True):
      initial_state = {
        'model': model,
        'messages': st.session_state['messages']
      }

      # thread_id enables the workflow to access previous messages from memory
      CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}

      # Generator expression filters stream to only AIMessage objects
      # and extracts content for typewriter-style rendering
      response = st.write_stream(
        msg.content for msg, _ in workflow.stream(
          input=initial_state, config=CONFIG, stream_mode='messages'
        )
        if isinstance(msg, AIMessage)
      )

      ai_message = AIMessage(content=response)
      st.session_state['messages'].append(ai_message)
