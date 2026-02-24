from typing import TypedDict

class BlogState(TypedDict):

    topic: str

    blog_outline: str

    blog_complete: str

    evaluation : str
    
    model: object