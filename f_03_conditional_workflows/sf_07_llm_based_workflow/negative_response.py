from review_state_schema import ReviewState

def negative_response(state: ReviewState) -> dict:
    '''
    This function generates a negative response for the review.
    '''

    diagnosis = state.diagnosis

    prompt = f"Generate a sorry response and apologize for the following review based on the diagnosis:\n\nReview: {state.review}\nDiagnosis: {diagnosis}\n\nResponse:"
    
    model = state.model

    response = model.invoke(prompt).content

    return {
        'response': response,
    }