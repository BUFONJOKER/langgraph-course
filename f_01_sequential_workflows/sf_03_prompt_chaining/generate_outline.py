from blog_state import BlogState

def generate_outline(state: BlogState) -> BlogState:
    '''
    generate outline of a blog from a given topic from llm and return state object with blog outline \n 
    '''

    topic = state['topic']

    prompt = f"Generate outline for a blog from this topic \n {topic}"

    model = state['model']

    result = model.invoke(prompt)

    result = result.content

    state['blog_outline'] = result

    return state