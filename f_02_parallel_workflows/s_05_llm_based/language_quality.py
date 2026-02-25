from essay_state import EssayState
from langchain_core.prompts import ChatPromptTemplate

def language_quality(state: EssayState) -> dict:
    '''
    Generate feedback and score based on language of quality and return dictionary with feedback and score
    '''

    SYSTEM_INSTRUCTIONS = """
    You are a professional linguistic editor and English professor. 
    Your goal is to assess the technical and stylistic quality of the writing.

    CRITICAL: You MUST output ONLY a valid JSON object with this exact structure:
    {{
        "feedback": "your detailed analysis here",
        "score": number_between_1_and_10
    }}
    No conversational headers, explanations, or Markdown code blocks.
    """

    USER_CONTENT = """
    Evaluate the following essay specifically for **Language Quality**:

    ---
    ESSAY:
    {essay}
    ---

    Focus your analysis on:
    1. **Vocabulary:** Diversity, precision, and appropriateness of word choice.
    2. **Grammar & Structure:** Grammatical correctness and variety in sentence construction.
    3. **Style & Flow:** Consistency of tone and the overall smoothness of transitions.

    Requirements:
    - Feedback: Provide your detailed analysis in the 'feedback' field.
    - Score: Provide a numerical score (1-10) in the 'score' field.
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
        'language_quality':result.feedback,
        'individual_scores':[result.score]
    }