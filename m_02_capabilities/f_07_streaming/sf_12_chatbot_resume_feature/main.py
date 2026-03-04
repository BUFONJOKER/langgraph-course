# ============================================================================
# IMPORTS
# ============================================================================
from model import load_model
from workflow import generate_workflow
from langchain_core.messages import HumanMessage, AIMessage
from thread_id import generate_thread_id
import streamlit as st


# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================
# thread_id persists across reruns, enabling conversation memory across sessions
if 'thread_id' not in st.session_state:
  st.session_state['thread_id'] = generate_thread_id()

if 'messages' not in st.session_state:
  st.session_state['messages'] = []


# ============================================================================
# UI SETUP of sidebar and main chat interface
# ============================================================================
st.header("Chatbot")
st.sidebar.title('Chatbot')
st.sidebar.button("New Chat")
st.sidebar.header("My Conversations")
st.sidebar.markdown(st.session_state['thread_id'])  # Display current thread_id for demonstration


# ============================================================================
# INITIALIZE MODEL & WORKFLOW
# ============================================================================
model = load_model()
workflow = generate_workflow()



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
