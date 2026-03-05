from pydantic import BaseModel, Field
from typing import List, Any, Literal

class DiagnosisOutput(BaseModel):

    '''
    Diagnosis Output class which inherits pydantic BaseModel. It has three fields, issue type, tone and urgency.
    1 - issue type is a literal field which can take values 'ux', 'bug','battery', 'other' and it describes the type of the issue in the review.
    2 - tone is a literal field which can take values 'angry', 'sad', 'neutral' and it describes the tone of the review.
    3 - urgency is a literal field which can take values 'low', 'medium', 'high' and it describes the urgency of the issue in the review.
    '''

    issue_type: Literal['ux', 'bug','battery', 'other'] = Field(description="Type of the issue")

    tone: Literal['angry', 'sad', 'neutral'] = Field(description="Tone of the review")

    urgency: Literal['low', 'medium', 'high'] = Field(description="Urgency of the issue")
