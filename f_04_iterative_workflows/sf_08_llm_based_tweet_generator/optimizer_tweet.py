from state_schema import TweetState
from langchain_core.prompts import ChatPromptTemplate

def optimize(state: TweetState) -> dict:
    '''
    This function is responsible for optimizing the generated tweet based on the feedback received from the evaluation step using LLM from huggingface meta-llama/Llama-3.1-8B-Instruct model.
    '''

    model = state['model']
    tweet = state['tweet']

    feedback = state['feedback']

    SYSTEM_INSTRUCTION = "You are a helpful assistant that optimizes tweets based on feedback."

    USER_CONTENT = '''
    Here is the generated tweet that needs optimization:
    {tweet}
    Please optimize the tweet based on the feedback:
    {feedback}
    provided in the previous evaluation step. Focus on improving the clarity, engagement, and relevance of the tweet while maintaining its original intent.
    '''

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_INSTRUCTION),
        ("user", USER_CONTENT)
    ])

    chain = prompt | model

    result = chain.invoke({
        "tweet": tweet,
        "feedback": feedback
    })

    iteration = state['iteration'] + 1

    return {
        "tweet": result.content,
        "tweet_history": [result.content],
        "iteration": iteration
    }
