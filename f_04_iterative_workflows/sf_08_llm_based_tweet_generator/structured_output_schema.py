from pydantic import BaseModel, Field
from typing import Literal

class TweetEvaluationOutput(BaseModel):
    '''
    Output schema for the evaluation step in the LLM-based tweet generator workflow. This schema captures the evaluation result and feedback for the generated tweet.
    '''

    evaluation: Literal['approved', 'needs_improvement'] = Field(..., description="The evaluation result of the generated tweet, indicating whether it meets the desired criteria or needs improvement")

    feedback: str = Field(default='', description="Feedback on the generated tweet, providing specific reasons for the evaluation result and suggestions for improvement if needed")