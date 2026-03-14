from langchain_core.messages import ToolMessage, HumanMessage, AIMessage

from model import load_embeddings_model, load_model
import streamlit as st
import os
from dotenv import load_dotenv
from typing import Dict, Any
from get_retriever import get_retriever
from tools import load_search_tool, calculator, get_stock_price, rag_tool
from workflow import build_workflow
from thread_id import generate_thread_id
from reset_chat import reset_chat
from add_thread_id import add_thread_id
from load_conversation import load_conversation
from ingest_pdf import ingest_pdf

from thread_document_metadata import thread_document_metadata


load_dotenv()

os.environ["LANGSMITH_PROJECT"] = "simple-chatbot-with-rag"

st.header("Simple Chatbot with RAG")


embeddings_model = load_embeddings_model(model_name="sentence-transformers/all-MiniLM-L6-v2")

model = load_model(model_name="qwen3.5:cloud")

tools_list = [load_search_tool(),calculator, get_stock_price, rag_tool]

workflow, llm_with_tools, all_threads = build_workflow(tools_list, model)
# -------------------Session State Initialization-------------------
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = all_threads

if 'ingested_docs' not in st.session_state:
    st.session_state['ingested_docs'] = {}

if 'retriever' not in st.session_state:
    st.session_state['retriever'] = ''

add_thread_id(st.session_state['thread_id'])

thread_key = st.session_state['thread_id']
thread_docs = st.session_state['ingested_docs'].setdefault(thread_key, {})
threads = st.session_state['chat_threads'][::-1]
selected_thread = None

# new chat button
if st.button("New Chat", type="secondary", use_container_width=True):
    reset_chat()
    st.rerun()

if thread_docs:
    lates_docs = list(thread_docs.keys())[-1]
    st.markdown(f"**Ingested Document:** {lates_docs}")

else:
    st.sidebar.info("**No document ingested yet. Please upload a PDF to start.**")

upload_file = st.sidebar.file_uploader("Upload a PDF document", type="pdf", accept_multiple_files=False, help="Upload a PDF document to use as the knowledge base for the chatbot.")

if upload_file:

    if upload_file.name in thread_docs:
        st.sidebar.warning(f"Document '{upload_file.name}' has already been ingested for this thread.")
    else:
        with st.sidebar.status("Ingesting document...",  expanded=True) as status_box:

            summary = ingest_pdf(upload_file.getvalue(), st.session_state['thread_id'], filename=upload_file.name)

            thread_docs[upload_file.name] = summary

            status_box.update(label="✅ PDF indexed", state="complete", expanded=False)

st.sidebar.subheader("Past Conversations")

if not threads:
    st.sidebar.info("No past conversations yet. Start by uploading a PDF and asking a question!")

else:
    for idx, thread in enumerate(threads):
        thread_label = str(thread[0]) if isinstance(thread, (tuple, list)) and thread else str(thread)
        if st.sidebar.button(thread_label, key=f"side-thread-{idx}-{thread_label}", use_container_width=True):
            selected_thread = thread_label


# --------------------- Main Chat Interface---------------------

st.title("Chat with your PDF Document or use tools!")

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

user_input = st.chat_input("Ask a question about the document or use tools...")

if user_input:
    st.session_state['message_history'].append({"role": "user", "content": user_input})

    with st.chat_message('user'):
        st.text(user_input)

    CONFIG = {
        'configurable':{'thread_id': thread_key},
        'metadata':{'thread_id': thread_key},
        'run_name':'chat_turn'
    }


    with st.chat_message('assistant'):
        status_holder = {'box': None}

        def ai_only_stream():
            for message_chunk, _ in workflow.stream({'model':llm_with_tools,'messages':[HumanMessage(content=user_input)]}, config=CONFIG, stream_mode='messages',):
                if isinstance(message_chunk, ToolMessage):
                    tool_name = getattr(message_chunk, "name", "tool")
                    if status_holder['box'] is None:
                        status_holder["box"] = st.status(f"Tool '{tool_name}' is being called...", state="running", expanded=True)
                    else:
                        status_holder['box'].update(label=f"Tool '{tool_name}' is being called...", state="running", expanded=True)
                if isinstance(message_chunk,AIMessage):
                    yield message_chunk.content
        ai_message = st.write_stream(ai_only_stream())

        if status_holder['box'] is not None:
            status_holder['box'].update(label="✅ Tool finished", state="complete", expanded=False)

    st.session_state['message_history'].append({"role": "assistant", "content": ai_message})

    doc_metadata = thread_document_metadata(thread_key)

    if doc_metadata:
        st.caption(
            f"Document indexed: {doc_metadata.get('filename')} "
            f"(chunks: {doc_metadata.get('chunks')}, pages: {doc_metadata.get('documents')})"
        )

st.divider()

if selected_thread:
    st.session_state['thread_id'] = selected_thread
    messages = load_conversation(selected_thread, workflow)

    temp_messages = []

    for msg in messages:
        role = 'user' if isinstance(msg, HumanMessage) else 'assistant'
        temp_messages.append({"role": role, "content": msg.content})

    st.session_state['message_history'] = temp_messages

    st.session_state['ingested_docs'].setdefault(selected_thread, {})
    st.rerun()