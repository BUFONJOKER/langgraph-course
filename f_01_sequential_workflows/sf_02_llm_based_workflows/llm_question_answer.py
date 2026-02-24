from llm_state_class import LLMState
from model_ollama import load_model

def llm_qa(state: LLMState) -> LLMState:

    question = state['question']

    prompt = f"Generate answer of following question \n {question}"

    model = load_model()

    result = model.invoke(prompt)

    result = result.content

    state['answer'] = result

    return state