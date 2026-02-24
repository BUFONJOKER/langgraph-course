from blog_state import BlogState

def generate_outline(state: BlogState) -> BlogState:

    topic = state['topic']

    prompt = f"Generate outline for a blog from this topic \n {topic}"

    model = state['model']

    result = model.invoke(prompt)

    result = result.content

    state['blog_outline'] = result

    return state