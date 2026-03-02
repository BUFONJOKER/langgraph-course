from state_schema import QuadraticState
from typing import Literal

def calculate_roots(state: QuadraticState) -> Literal['distinct_roots', 'repeated_root', 'complex_roots']:
    '''
    From discriminant value check roots
    '''

    discriminant = state.discriminant

    if discriminant > 0:
        return 'distinct_roots'

    elif discriminant == 0:
        return 'repeated_root'

    else:
        return 'complex_roots'