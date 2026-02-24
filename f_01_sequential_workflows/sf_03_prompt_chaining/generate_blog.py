from blog_state import BlogState

def generate_blog(state: BlogState) -> BlogState:
    '''
    Generate a detailed blog from a given topic and outline and return a state object with complete blog
    '''

    topic = state['topic']

    outline = state['blog_outline']

    prompt = f"Generate Blog on a title {topic} from this outline \n {outline}"

    model = state['model']

    result = model.invoke(prompt)

    result = result.content

    state['blog_complete'] = result

    return state