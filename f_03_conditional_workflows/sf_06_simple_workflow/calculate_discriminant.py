from state_schema import QuadraticState

def calculate_discriminant(state: QuadraticState) -> dict:
    '''
    Calculate discriminant of a,b,c
    '''

    a = state.a
    b = state.b
    c = state.c

    discriminant = (b**2) - (4 * (a * c))

    return {
        'discriminant':round(discriminant, 2)
    }

