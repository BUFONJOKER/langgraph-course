from thread_id import generate_thread_id
from add_thread_id import add_thread_id
import streamlit as st

def reset_chat():
    '''Resets the chat by clearing the session state and generating a new thread ID.'''

    thread_id = generate_thread_id()

    st.session_state['thread_id'] = thread_id

    add_thread_id(st.session_state['thread_id'])

    st.session_state['messages'] = []

