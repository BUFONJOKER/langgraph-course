# ----- Chatbot Application with Conversation Memory in SQLite Database
# ----- using Streamlit and LangGraph



# ============================================================================
# IMPORT necessary libraries and functions for the chatbot application
# ============================================================================

from model import load_model
from workflow import generate_workflow
from langchain_core.messages import HumanMessage, AIMessage, AIMessageChunk, ToolMessage
from thread_id import generate_thread_id
from reset_chat import reset_chat
from add_thread import add_thread
from load_conversation import load_conversation
from langgraph.prebuilt import ToolNode
from dotenv import load_dotenv
from tools import load_search_tool, calculator, get_stock_price
from extract_tool_names import extract_tool_names
import streamlit as st
import os

os.environ['LANGSMITH_PROJECT'] = 'Chatbot with tools'

load_dotenv()



# app icon and title setup
st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")
st.title("Chatbot with Conversation Memory")

# ============================================================================
# INITIALIZE MODEL & WORKFLOW
# ============================================================================
tools_list = [load_search_tool, calculator, get_stock_price]

model = load_model()

llm_with_tools = model.bind_tools(tools_list)

tool_node = ToolNode(tools=tools_list)

workflow, all_threads = generate_workflow(tool_node)


# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================
# thread_id persists across reruns, enabling conversation memory across sessions
if 'thread_id' not in st.session_state:
  st.session_state['thread_id'] = generate_thread_id()

if 'messages' not in st.session_state:
  st.session_state['messages'] = []

if 'chat_threads' not in st.session_state:
  st.session_state['chat_threads'] = all_threads  # Initialize with threads from database

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
    initial_state = {
      'model': llm_with_tools,
      'messages': st.session_state['messages']
    }

    # thread_id enables the workflow to access previous messages from memory
    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}

    tool_status_container = st.container()
    response_placeholder = st.empty()
    response_chunks = []
    tool_names = []
    tool_status = None

    try:
      for msg, metadata in workflow.stream(
        input=initial_state, config=CONFIG, stream_mode='messages'
      ):
        for tool_name in extract_tool_names(msg):
          if tool_name not in tool_names:
            tool_names.append(tool_name)

            if tool_status is None:
              with tool_status_container:
                tool_status = st.status('Using tools...', state='running', expanded=True)

            tool_status.write(f'Tool requested: {tool_name}')
            tool_status.update(
              label=f"Using tool: {tool_name}",
              state='running',
              expanded=True
            )

        if isinstance(msg, ToolMessage) and tool_status is not None:
          completed_tool = msg.name or metadata.get('langgraph_node', 'tool')
          tool_status.write(f'Tool finished: {completed_tool}')

        if isinstance(msg, AIMessageChunk) and isinstance(msg.content, str) and msg.content:
          response_chunks.append(msg.content)
          response_placeholder.markdown(''.join(response_chunks))

      response = ''.join(response_chunks)

      if tool_status is not None:
        completed_tools = ', '.join(tool_names)
        tool_status.update(
          label=f"Completed tool run: {completed_tools}",
          state='complete',
          expanded=False
        )

      ai_message = AIMessage(content=response)
      st.session_state['messages'].append(ai_message)

    except Exception:
      if tool_status is not None:
        tool_status.update(label='Tool execution failed', state='error', expanded=True)
      raise
