from langgraph.graph import StateGraph, START, END
from blog_state import BlogState
from generate_outline import generate_outline
from generate_blog import generate_blog
from evaluation import evaluation
from model import load_model
import streamlit as st

st.title("Blog Generator")

model = load_model()

graph = StateGraph(state_schema=BlogState)

graph.add_node('generate_outline', generate_outline)

graph.add_node('generate_blog', generate_blog)

graph.add_node('evaluation', evaluation)

graph.add_edge(start_key=START, end_key='generate_outline')

graph.add_edge(start_key='generate_outline', end_key='generate_blog')

graph.add_edge(start_key='generate_blog', end_key='evaluation')

graph.add_edge(start_key='evaluation', end_key=END)

workflow = graph.compile()

input_text = st.text_input("Write Blog Title : ")

input_state = {
    'topic': str(input_text),
    'model': model
}

if st.button(label="Generate", type='primary'):

    with st.spinner("Generating", show_time=True):
        
        blog = workflow.invoke(input=input_state)

    st.write(blog['blog_complete'])

    st.divider()

    st.divider()

    st.write("*"*50)

    st.header("Evaluation")

    st.write(blog['evaluation'])