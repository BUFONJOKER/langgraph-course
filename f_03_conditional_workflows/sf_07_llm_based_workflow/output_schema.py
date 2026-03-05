from pydantic import  BaseModel, Field
from typing import  Literal

class SentimentSchema(BaseModel):
    '''
    SentimentScheme based on which model will return the sentiment of the review
    positive or negative
    '''
    sentiment: Literal['positive', 'negative'] = Field(description='sentiment of review')