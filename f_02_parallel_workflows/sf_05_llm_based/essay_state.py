from pydantic import BaseModel, Field
from typing import Annotated, Any
import operator

class EssayState(BaseModel):
    '''
    EssayState class which inherits pydantic BaseModel with variables
    essay (str)
    model (Any)
    structured_model (Any)
    clarity_of_thoughts (str)
    deep_analysis (str)
    language_quality (str)
    overall_feedback (str)
    individual_scores (list of  int)
    avg_score (float)
    '''

    essay: str = Field(description="Essay given by user to evaluate")

    model: Any = Field(description="LLM used to generate feedbacks")

    structured_model: Any = Field(description="LLM with structured output")

    clarity_of_thoughts: str = Field(
        default = '', description="Feedback of essay based on clarity of thoughts in essay"
    )

    deep_analysis: str = Field(default = '', description="Deep analysis of essay")

    language_quality: str = Field(default = '', description="Language quality used in essay")

    overall_feedback: str = Field(
        default = '', description="Summary of overall feedback of essay"
    )

    individual_scores: Annotated[list[float], operator.add] = Field(
        default_factory=list, description="Scores of all feedback on a scale of 1 to 10"
    )

    avg_score: float = Field(default=0.0, description="Average scores of all feedbacks")