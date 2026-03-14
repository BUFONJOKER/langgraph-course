import streamlit as st

def add_thread_id(thread_id):
    '''Adds a thread ID to the session state if it doesn't already exist. This can be used to track conversations or sessions in the chatbot.'''

    if "thread_id" not in st.session_state['chat_threads']:

        st.session_state['chat_threads'].append(thread_id)