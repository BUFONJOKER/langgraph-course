from state_schema import TweetState
from langchain_core.prompts import ChatPromptTemplate

def generate(state: TweetState) -> dict:
    '''
    This function is responsible for generating a tweet using LLM from huggingface meta-llama/Llama-3.1-8B-Instruct model. 
    '''
    
    model = state['model']
    topic = state['topic']

    SYSTEM_INSTRUCTIONS = """
    You are a creative and witty social media content creator. Your task is to generate an engaging and concise tweet based on the provided topic. The tweet should be attention-grabbing, relevant to the topic, and encourage interaction from followers.
    """

    USER_CONTENT = """
    Generate a tweet based on the following topic:
    ---
    TOPIC:
    {topic}
    ---
    Requirements:
    - The tweet should be no more than 280 characters.
    - It should be engaging and encourage interaction.
    - Use appropriate hashtags and mentions where relevant.
    """

    prompt_template = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_INSTRUCTIONS),
            ("user", USER_CONTENT)
        ]
    )

    chain = prompt_template | model
    
    tweet = chain.invoke({"topic": topic})

    return {
        "tweet": tweet.content, 'tweet_history': [tweet.content]
    }