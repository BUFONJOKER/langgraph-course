from thread_id import generate_thread_id
from add_thread import add_thread
import streamlit as st

def reset_chat():
  '''
  Resets the chat by clearing the session state for messages and thread_id.
  '''

  thread_id = generate_thread_id()  # Generate a new thread_id for the new conversation
  st.session_state['thread_id'] = thread_id  # Update session state with new thread

  add_thread(st.session_state['thread_id'])  # Add the new thread_id to the list of chat threads
  st.session_state['messages'] = []  # Clear chat messages to reset the conversation
