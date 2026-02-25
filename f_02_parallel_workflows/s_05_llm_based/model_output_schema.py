from pydantic import BaseModel, Field

class OutputSchema(BaseModel):
    '''
    Schema based on which llm should produced output
    feedback (str)
    score (int)
    '''

    feedback: str = Field(description="Detailed feedback for essay")

    score: float = Field(description="Score on scale of 1 to 10", ge=1.0, le=10.0)