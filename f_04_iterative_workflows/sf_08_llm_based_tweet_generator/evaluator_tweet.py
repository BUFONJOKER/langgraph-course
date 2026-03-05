from state_schema import TweetState
from langchain_core.prompts import ChatPromptTemplate

def evaluate(state: TweetState) -> dict:
    '''
    This function is responsible for evaluating the generated tweet using LLM qwen3-next:80b-cloud model from ollama. 
    '''

    structured_model = state['structured_model']

    tweet = state['tweet']

    SYSTEM_INSTRUCTION = """You are a ruthless and critical tweet evaluator. Your task is to evaluate the given tweet.
    """

    USER_CONTENT = """Evaluate the following tweet based on the criteria mentioned above:
    Tweet: {tweet}

    The tweet should be evaluated based on the following criteria:
    1. Relevance: The tweet should be relevant to the given topic.
    2. Clarity: The tweet should be clear and easy to understand.
    3. Engagement: The tweet should be engaging and interesting to the audience.
    4. Conciseness: The tweet should be concise and to the point, ideally under 280 characters.
    5. Creativity: The tweet should be creative and original, avoiding clichés and common phrases.
    The evaluation should be based on the above criteria, and the output should be either 'approved' if the tweet meets the criteria or 'needs_improvement'.
    """

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_INSTRUCTION),
        ("user", USER_CONTENT)
    ])

    chain = prompt | structured_model

    result = chain.invoke({"tweet": tweet})

    return {"evaluation": result.evaluation, "feedback": result.feedback, 'feedback_history':[result.feedback]}