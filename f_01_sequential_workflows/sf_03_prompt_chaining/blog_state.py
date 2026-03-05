from typing import TypedDict

class BlogState(TypedDict):
    '''
    BlogState class which inherit TypedDict from typing module
    having variables
    - topic (str)
    - blog_outline (str)
    - blog_complete (str)
    - evaluation(str)
    - model (object)
    '''

    topic: str

    blog_outline: str

    blog_complete: str

    evaluation : str
    
    model: object