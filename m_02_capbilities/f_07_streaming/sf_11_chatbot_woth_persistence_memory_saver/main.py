from model import load_model
from workflow import generate_workflow
from langchain_core.messages import HumanMessage, AIMessage
import streamlit as st

st.header("Chatbot")

# config for in memory saver
CONFIG = {'configurable':{'thread_id':'1'}}

model = load_model()

workflow = generate_workflow()


if 'messages' not in st.session_state:
  st.session_state['messages'] = []

for message in st.session_state['messages']:

  role = 'user' if isinstance(message, HumanMessage) else 'assistant'

  with st.chat_message(role):
    st.markdown(message.content)

if prompt := st.chat_input("Ask anything to AI assistant"):

  with st.chat_message('user'):
    st.markdown(prompt)

  user_message = HumanMessage(content=prompt)
  st.session_state['messages'].append(user_message)

  with st.chat_message('assistant'):

    with st.spinner("Generating response...", show_time=True):

      initial_state = {
        'model':model,
        'messages':st.session_state['messages']
      }

      # getting response in stream like typewriter type and check if response is have AIMessage and then extract its content
      response = st.write_stream(

      msg.content for msg, _ in workflow.stream(
         input=initial_state, config=CONFIG, stream_mode='messages'
      )

      if isinstance(msg, AIMessage)

      )

      ai_message = AIMessage(content=response)

      st.session_state['messages'].append(ai_message)
