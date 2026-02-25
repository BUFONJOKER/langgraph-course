from review_state_schema import ReviewState

def positive_response(state: ReviewState) -> dict:
    '''
    This function generates a positive response to thank the customer for their feedback and encourage them to share their experience with others.
    '''

    review = state.review

    prompt = f"""Generate a response to thank the customer for their \n {review} and encourage them to share their experience with others."""

    model = state.model

    response = model.invoke(prompt).content

    return {
        'response': response,
    }