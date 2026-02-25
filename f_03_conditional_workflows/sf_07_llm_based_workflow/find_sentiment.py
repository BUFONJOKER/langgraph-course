from review_state_schema import ReviewState

def find_sentiment(state: ReviewState) -> dict:

    '''
    This function takes the review state as input and returns the review state with the sentiment of the review. It uses the structured model to find the sentiment of the review and updates the sentiment field of the review state.
    '''

    model = state.structured_model

    review = state.review

    prompt = f"What is the sentiment of following review - {review}"

    result = model.invoke(prompt)

    output = result.sentiment

    return {
        'sentiment': output
    }
