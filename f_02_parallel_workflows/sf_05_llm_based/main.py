from model import load_model
from model_output_schema import OutputSchema
from essay_state import EssayState
from clarity_of_thoughts import clarity_of_thoughts
from deep_analysis import deep_analysis
from language_quality import language_quality
from overall_feedback import overall_feedback
# from input_essay import essay
from langgraph.graph import StateGraph, START, END
import streamlit as st

st.set_page_config(page_title="Essay Evaluator")
st.title("✍️ Academic Essay Evaluator")

@st.cache_resource
def generate_workflow():

    model = load_model()

    structured_model = model.with_structured_output(
        schema=OutputSchema, method='json_mode'
    )

    graph = StateGraph(state_schema=EssayState)

    graph.add_node('clarity_of_thoughts', clarity_of_thoughts)
    graph.add_node('deep_analysis', deep_analysis)
    graph.add_node('language_quality', language_quality)
    graph.add_node('overall_feedback', overall_feedback)

    graph.add_edge(START, 'clarity_of_thoughts')
    graph.add_edge(START, 'deep_analysis')
    graph.add_edge(START, 'language_quality')

    graph.add_edge('clarity_of_thoughts', 'overall_feedback')
    graph.add_edge('deep_analysis', 'overall_feedback')
    graph.add_edge('language_quality', 'overall_feedback')


    graph.add_edge('overall_feedback', END)


    workflow = graph.compile()

    return workflow, model, structured_model

workflow, model, structured_model = generate_workflow()

essay = st.text_area("Paste your essay here:", height=300, placeholder="Type or paste your essay content...")



if st.button("Analyze Essay", type='primary'):
    if not essay.strip():
        st.warning("Please enter some text first.")
    else:
        input_state = {
            'essay':essay,
            'model':model,
            'structured_model':structured_model
        }
        
        with st.spinner("Our AI experts are reviewing your work...", show_time=True):
            # Execute the LangGraph workflow
            output = workflow.invoke(input_state)
            
            # Display results
            st.divider()
            
            st.header(f"Qwen3-next:80b used")
            # Evaluation Metrics
            col1, col2, col3 = st.columns(3)
            # individual_scores is a list populated by operator.add from three nodes
            scores = output.get('individual_scores', [0, 0, 0])
            
            with col1:
                st.metric("Clarity", f"{scores[0]}/10")
            with col2:
                st.metric("Depth", f"{scores[1]}/10")
            with col3:
                st.metric("Language", f"{scores[2]}/10")

            st.divider()

            # Detailed Feedback Expanders
            with st.expander("🔍 Clarity Analysis"):
                st.write(output.get('clarity_of_thoughts'))

            with st.expander("🧠 Intellectual Depth"):
                st.write(output.get('deep_analysis'))

            with st.expander("✍️ Linguistic Quality"):
                st.write(output.get('language_quality'))

            # Final Summary
            st.header("Overall Feedback")
            st.write(output['overall_feedback'])
            st.subheader(f"Final Average Score: {output.get('avg_score', 0):.2f}")