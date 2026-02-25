from state_schema import QuadraticState

def distinct_roots(state: QuadraticState) -> dict:
    '''
    calculate two distinct real roots
    '''

    a = state.a
    b = state.b
    c = state.c
    discriminant = state.discriminant

    root_1 = (-b + discriminant**0.5) / (2*a)
    root_2 = (-b - discriminant**0.5) / (2*a)

    result = f"Two distinct real roots are {root_1} and {root_2}"

    return {
        'result':result
    }