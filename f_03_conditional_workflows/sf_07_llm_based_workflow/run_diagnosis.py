from review_state_schema import ReviewState

def run_diagnosis(state: ReviewState) -> dict:
    '''
    Run diagnosis function takes the review state as input and returns the diagnosis of the review. It uses the diagnois_model to find the diagnosis of the review. The prompt for the model is generated using the review from the state. The diagnosis is returned as a dictionary.
    '''

    prompt = f"""The customer has left a negative review: \n {state.review} \n Diagnose the issue_type, tone and urgency of the issue in the review."""

    model = state.diagnois_model

    diagnosis = model.invoke(prompt)

    return {
        'diagnosis': diagnosis.model_dump(),
    }