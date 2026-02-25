from pydantic import BaseModel, Field

class QuadraticState(BaseModel):
    '''
    QuadraticState class which inherits pydantic BaseModel class with variables
    a (float)
    b (float)
    c (float)
    show_equation (str) 
    discriminant (float)
    result (str)
    '''

    a: float = Field(description="Value of a")
    b: float = Field(description="Value of b")
    c: float = Field(description="Value of c")

    show_equation: str = Field(default='', description='Quadratic equation')
    discriminant: float = Field(default=0.0, description='Discriminant')
    result: str = Field(default='', description='Final result')