from state_schema import QuadraticState

def show_equation(state: QuadraticState) -> dict:
    '''
    Show quadratic equation based on a, b, c
    '''

    a = state.a
    b = state.b
    c = state.c

    b_str = '+ '+str(b) if b>0 else '- '+str(-1*b)
    c_str = '+ '+str(c) if c>0 else '- '+str(-1*c)

    equation = f"{a}x² {b_str}x {c_str}"

    return {
        'equation':equation
    }

