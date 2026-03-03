from review_state_schema import ReviewState
from typing import Literal

def check_sentiment(state: ReviewState) -> Literal['positive_response', 'run_diagnosis']:
    '''
    This function checks the sentiment of the review and returns the next node to execute based on the sentiment.
    '''
    sentiment = state.sentiment

    if sentiment == 'positive':
        return 'positive_response'
    
    else:
        return 'run_diagnosis'