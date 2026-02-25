from state_schema import QuadraticState

def repeated_root(state: QuadraticState) -> dict:
    '''
    calculate one real repeated root
    '''
    
    a = state.a
    b = state.b

    root = (-b) / (2*a)
   
    result = f"One real repeated root is {root}"

    return {
        'result':result
    }