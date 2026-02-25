from batsmen_state import BatsmenState

def strike_rate(state: BatsmenState) -> dict:
    '''
    Calculate strike rate from given data balls, runs and return computed field
    '''
    balls = state.balls

    runs = state.runs

    result = (runs / balls) * 100

    output = {"strike_rate": round(result, 2)}

    return output