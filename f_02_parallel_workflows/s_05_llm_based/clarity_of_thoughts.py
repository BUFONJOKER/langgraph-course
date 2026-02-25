from essay_state import EssayState
from langchain_core.prompts import ChatPromptTemplate

def clarity_of_thoughts(state: EssayState) -> dict:
    '''
    Generate feedback and score based on clarity of thought and return dictionary with feedback and score
    '''

    SYSTEM_INSTRUCTIONS = """
    You are a specialized academic grader. 
    Your task:
    1. Provide structured feedback.
    2. Provide a numerical score (1-10).

    CRITICAL: You MUST output ONLY a valid JSON object with this exact structure:
    {{
        "feedback": "your detailed analysis here",
        "score": number_between_1_and_10
    }}
    No conversational filler, no markdown, no explanations outside the JSON.
    """

    USER_CONTENT = """
    Analyze the **Clarity of Thoughts** in the following essay:

    ---
    ESSAY:
    {essay}
    ---

    Evaluation Rubric:
    - Logical progression of ideas.
    - Strength and placement of the thesis.
    - Coherence between arguments.
    """

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ('system', SYSTEM_INSTRUCTIONS),
            ('user', USER_CONTENT)
        ]
    )

    chain = prompt_template | state.structured_model

    result = chain.invoke({'essay':state.essay})


    return {
        'clarity_of_thoughts':result.feedback,
        'individual_scores':[result.score]
    }