from typing import TypedDict, Annotated, List, Literal
from pydantic import Field
import operator

class TweetState(TypedDict):
    '''
    State schema for the LLM-based tweet generator workflow. This schema captures the topic, generated tweet, evaluation results, feedback, iteration count, and history of generated tweets and feedback.
    '''

    topic: str = Field(default='', description="The topic for which the tweet is being generated")

    tweet: str = Field(default='', description="The generated tweet")

    evaluation: Literal['approved', 'needs_improvement'] = Field(default='', description="The evaluation result of the generated tweet")

    feedback: str = Field(default='', description="Feedback on the tweet")

    iteration: int = Field(default=0, description="The current iteration number")

    max_iterations: int = Field(default=5, description="The maximum number of iterations allowed")

    tweet_history: Annotated[List[str], operator.add] = Field(default_factory=list, description="History of generated tweets")
    feedback_history: Annotated[List[str], operator.add] = Field(default_factory=list, description="History of feedback provided")