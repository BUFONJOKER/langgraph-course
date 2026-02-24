from blog_state import BlogState

def evaluation(state: BlogState) -> BlogState:

    outline = state['blog_outline']

    blog = state['blog_complete']

    model = state['model']

    prompt = f"Based on this outline \n {outline}. Evaluate and rate my blog \n {blog} on scale of 1 to 10 and also write a short review"

    result = model.invoke(prompt)

    result = result.content

    state['evaluation'] = result

    return state