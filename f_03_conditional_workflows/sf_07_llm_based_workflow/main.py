from output_schema import SentimentSchema
from model import load_model
from langgraph.graph import StateGraph, START, END
from review_state_schema import ReviewState
from find_sentiment import find_sentiment
from negative_response import negative_response
from run_diagnosis import run_diagnosis
from check_sentiment import check_sentiment
from positive_response import positive_response
from diagonsis_output_schema import DiagnosisOutput
import streamlit as st

st.set_page_config(page_title="LLM Based Workflow", page_icon=":robot_face:")
st.title("Review Analysis Workflow with LLMs")

@st.cache_resource
def generate_workflow():
    model = load_model()

    structured_model = model.with_structured_output(
        schema=SentimentSchema, method='function_calling'
    )

    diagnois_model = model.with_structured_output(
        schema=DiagnosisOutput, method='function_calling'
    )

    graph = StateGraph(ReviewState)

    graph.add_node('find_sentiment', find_sentiment)
    graph.add_node('run_diagnosis', run_diagnosis)
    graph.add_node('positive_response', positive_response)
    graph.add_node('negative_response', negative_response)


    graph.add_edge(START, 'find_sentiment')
    graph.add_conditional_edges('find_sentiment',check_sentiment)
    graph.add_edge('positive_response', END)
    graph.add_edge('run_diagnosis', 'negative_response')
    graph.add_edge('negative_response', END)
    graph.add_edge('find_sentiment', END)

    workflow = graph.compile()

    return workflow, model, structured_model, diagnois_model

workflow, model, structured_model, diagnois_model = generate_workflow()

review = st.text_input("Enter the review to analyze:")

if st.button("Analyze Review", type='primary'):
    input_state = {
        'model': model,
        'review': review,
        'structured_model': structured_model,
        'diagnois_model': diagnois_model
    }

    with st.spinner("Analyzing the review...", show_time=True):
        output = workflow.invoke(input_state)


    # Create a clean header with the model info in a small caption or subheader
    st.markdown("# 📊 Review Analysis Result")
    st.markdown(f"#### Powered by: {model.model}")

    st.divider()

    # --- Top Row: Sentiment Metric ---
    # Using columns lets the sentiment stand out without taking up vertical space
    st.markdown("## 📊 Sentiment")
    if output['sentiment'] == 'positive':
        st.markdown("#### 😊 Positive")
    
    elif output['sentiment'] == 'negative':
        st.markdown("#### 😞 Negative")

    st.markdown(f"#### The sentiment of the review is **{output['sentiment']}**.")

    st.divider()

    
    # Tables are good, but sometimes a dataframe looks cleaner in Streamlit
    if output['sentiment'] == 'negative':
        # --- Middle Section: Diagnosis ---
        st.markdown("## 🔍 Review Diagnosis")
        diagnois = output['diagnosis']

        for key, val in diagnois.items():
            st.markdown(f"#### {key.capitalize()} --- {val}")

        st.divider()

    # --- Bottom Section: Response ---
    st.markdown("## ✉️ Suggested Response")
   
    with st.container(border=True):
        st.write(output['response'])
        

