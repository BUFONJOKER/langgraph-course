from essay_state import EssayState
from langchain_core.prompts import ChatPromptTemplate

def deep_analysis(state: EssayState) -> dict:
    '''
    Generate feedback and score based on deep analysis and return dictionary with feedback and score
    '''

    SYSTEM_INSTRUCTIONS = """
    You are a senior academic critic. Your role is to evaluate the intellectual 
    depth and argumentative rigor of the text.

    CRITICAL: You MUST output ONLY a valid JSON object with this exact structure:
    {{
        "feedback": "your detailed analysis here",
        "score": number_between_1_and_10
    }}
    No conversational headers, no markdown, no explanations outside the JSON.
    """

    USER_CONTENT = """
    Perform a **Deep Analysis** of the following essay:

    ---
    ESSAY:
    {essay}
    ---

    Focus your evaluation on these key pillars:
    1. **Depth of Argument:** Does the writer explore the "why" and "how" rather than just stating facts?
    2. **Evidence & Support:** Are claims backed up by logical reasoning or specific examples?
    3. **Counter-arguments:** Does the writer acknowledge or address alternative perspectives?

    Requirements:
    - Provide feedback in the 'feedback' field.
    - Provide a score (1-10) in the 'score' field.
    """

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ('system', SYSTEM_INSTRUCTIONS),
            ('user', USER_CONTENT)
        ]
    )

    chain = prompt_template | state.structured_model

    result = chain.invoke({'essay':state.essay})

    return  {
        'deep_analysis':result.feedback,
         'individual_scores':[result.score]
    }