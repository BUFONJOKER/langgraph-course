from pydantic import BaseModel, Field
from typing import Literal, Any

class ReviewState(BaseModel):

    '''
    Review State class which inherits pydantic BaseModel. It has four fields, 
    model, structured model, review and sentiment.
    1 - Model is a field which takes the LLM model which is used to find the sentiment of the review.
    2 - Structured model is a field which takes the LLM model and produced structured output . 
    3 - Response is a string field which describes the response to the review.
    4 - Review is a string field which describes the review whose sentiment is to find.
    5 - Sentiment is a literal field which can take values 'positive' or 'negative' and it describes the sentiment of the review.
    '''

    model : Any = Field(description="LLM model to find sentiment of review")
    
    structured_model : Any = Field(description="LLM model with structured output to find sentiment of review")

    diagnois_model : Any = Field(description="LLM model with structured output to find diagnosis of review")
    
    diagnosis: dict = Field(default={}, description="Diagnosis of the review")

    review: str = Field(description="Review whose sentiment is to find")
    
    response: str = Field(default='', description='Response to the review')

    sentiment: Literal['positive','negative'] = Field(default='', description='Sentiment of review')