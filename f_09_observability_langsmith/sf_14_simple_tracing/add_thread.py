import streamlit as st

def add_thread(thread_id):
  '''
  Adds a new thread_id to the session state list of chat threads.
  '''
  if thread_id not in st.session_state['chat_threads']:
    st.session_state['chat_threads'].append(thread_id)