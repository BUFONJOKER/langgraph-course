from essay_state import EssayState
from langchain_core.prompts import ChatPromptTemplate

def overall_feedback(state: EssayState) -> dict:
    '''
    Overall feedback of essay based on all three feedbacks
    deep_analysis
    clarity_of_thoughts
    language_quality
    '''


    SYSTEM_INSTRUCTIONS = """
    You are a final grading supervisor and academic mentor. 
    Your job is to read multiple feedback points and synthesize them into a 
    single, professional, and encouraging summary for a student.

    STRICT RULES:
    1. Do not repeat the individual scores.
    2. Focus on synthesis and narrative flow.
    4. Use the 'feedback' field for the summary.
    """

    USER_CONTENT = """
    Summarize the following evaluation components into a single, cohesive **Overall Feedback** report:

    ---
    EVALUATION COMPONENTS:
    1. Clarity of Thoughts: {clarity}
    2. Language Quality: {language}
    3. Deep Analysis: {analysis}
    ---

    TASK:
    - Highlight the main strength of the essay.
    - Identify the primary area for improvement based on the three reports.
    - Provide a concluding encouraging remark.
    """

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ('system', SYSTEM_INSTRUCTIONS),
            ('user', USER_CONTENT)
        ]
    )

    chain = prompt_template | state.model

    result = chain.invoke(
        {
            'clarity': state.clarity_of_thoughts,
            'language': state.language_quality,
            'analysis': state.deep_analysis
        }
    )

    # Calculate average score from individual scores
    avg_score = sum(state.individual_scores) / len(state.individual_scores) if state.individual_scores else 0.0

    return {
        'overall_feedback': result.content,
        'avg_score': round(avg_score, 2)
    }