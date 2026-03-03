from state_schema import QuadraticState

def complex_roots(state: QuadraticState) -> dict:
    '''
    calculate two complex roots
    '''

    a = state.a
    b = state.b
    c = state.c
    discriminant = state.discriminant

    root_1 = (-b + ((-1**0.5)* (discriminant**0.5))) / (2*a)
    root_2 = (-b - ((-1**0.5)* (discriminant**0.5))) / (2*a)

    result = f"Two complex roots are {root_1} and {root_2}"

    return {
        'result':result
    }