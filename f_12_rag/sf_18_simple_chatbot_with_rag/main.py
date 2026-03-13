from document_loader import load_pdf
from document_splitter import split_documents
from generate_embeddings import embeddings
from retriever import retrieve
from model import load_embeddings_model, load_model
from langchain_community.tools import tool
from state_schema import ChatState
from langgraph.prebuilt import tools_condition, ToolNode
from chat_node import chat_node
from langgraph.graph import StateGraph, START, END
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGSMITH_PROJECT"] = "simple-chatbot-with-rag"

st.header("Simple Chatbot with RAG")

upload_file = st.file_uploader("Upload a PDF document", type="pdf", accept_multiple_files=False, help="Upload a PDF document to use as the knowledge base for the chatbot.")

embeddings_model = load_embeddings_model(model_name="sentence-transformers/all-MiniLM-L6-v2")

model = load_model(model_name="qwen3.5:cloud")



@st.cache_resource
def get_retriever(file_path):
    # Load the PDF document
    documents = load_pdf(file_path)

    # split the document into smaller chunks
    split_docs = split_documents(documents)

    # Generate embeddings for the document chunks and create a vector store
    vector_store = embeddings(embeddings_model, split_docs)

    # Create a retriever from the vector store
    retriever = retrieve(vector_store)

    return retriever

if upload_file is not None:

    file_path = upload_file.name

    with open(file_path, "wb") as f:

        f.write(upload_file.getbuffer())

    retriever = get_retriever(file_path)

@tool
def rag_tool(query: str):
    '''This function is a tool to retrieve relevant information from the vector store using the retriever.'''

    result = retriever.invoke(query)

    context = [doc.page_content for doc in result]
    metadata = [doc.metadata for doc in result]

    return {
        'query': query,
        'context': context,
        'metadata': metadata
        }

tools_list = [rag_tool]

@st.cache_resource
def build_workflow():
    '''This function builds the workflow for the RAG chatbot using LangGraph. It creates a state graph with a chat node and a tool node, and defines the edges between them based on the tools_condition.'''
    llm_with_tools = model.bind_tools(tools_list)

    tool_node = ToolNode(tools_list)

    graph = StateGraph(ChatState)

    graph.add_node('chat_node', chat_node)
    graph.add_node('tools', tool_node)

    graph.add_edge(START, 'chat_node')
    graph.add_conditional_edges('chat_node', tools_condition)
    graph.add_edge('tools', 'chat_node')
    graph.add_edge('chat_node', END)

    workflow = graph.compile()

    return workflow, llm_with_tools

if upload_file:
    question = st.text_input("Ask a question about the document: ")

    if st.button("Get Answer", type="primary"):

        with st.spinner("Processing...", show_time=True):

            workflow, llm_with_tools = build_workflow()
            messages = [
                {"role": "user", "content": question},
            ]

            initial_state = {
                'model':llm_with_tools,
                'messages': messages
            }

            result = workflow.invoke(initial_state)

            st.markdown(result['messages'][-1].content)